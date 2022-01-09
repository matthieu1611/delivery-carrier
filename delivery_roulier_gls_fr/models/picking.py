# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging
from datetime import date

from odoo import fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


INCOTERM_MAPPING = {
    "DDP": "10",
    "DAP": "20",
}


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def _gls_fr_rest_get_to_address(self, package=None):
        address = self._roulier_get_to_address(package=package)
        (
            address["street"],
            address["street2"],
            address["street3"],
        ) = self.partner_id._get_split_address(3, 35)
        return address

    def _gls_fr_rest_get_service(self, account, package=None):
        result = self._roulier_get_service(account, package=package)
        result.update({
            # should probably renamed contactId in roulier
            "agencyId": account.gls_fr_rest_contact_id,
            "customerId": account.gls_fr_rest_customer_id,
            "intructions": self.note or "",
            "consignee_ref": self.name[:20],
            "reference_1": self.origin[:20],
            "reference_2": self.name[:20],
        })
        incoterm_code = self._get_gls_incoterm()
        if incoterm_code:
            result["incoterm"] = incoterm_code
        return result

    def _get_gls_incoterm(self):
        self.ensure_one()
        incoterm = self.sale_id.incoterm
        gls_code = ""
        if incoterm:
            gls_code = INCOTERM_MAPPING.get(incoterm.code, "")
        return gls_code

