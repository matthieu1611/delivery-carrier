# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def _ups_rest_get_service(self, account, package=None):
        vals = self._roulier_get_service(account, package=package)
        vals["reference1"] = self.origin or self.name
        return vals

    def _ups_rest_get_auth(self, account, package=None):
        vals = self._roulier_get_auth(account, package=package)
        vals["shipper_number"] = account.ups_rest_shipper_number
        vals["license_number"] = account.ups_rest_license_number
        vals["transaction_source"] = "Odoo - %s" % self.env.cr.dbname
        return vals
