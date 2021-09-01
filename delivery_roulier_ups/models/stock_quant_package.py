# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class StockQuantPackage(models.Model):
    _inherit = "stock.quant.package"

    def _ups_rest_should_include_customs(self, picking):
        return False

    def _ups_rest_get_tracking_link(self):
        return (
            "https://ups.com/WebTracking/track?trackingNumber=%s" % self.parcel_tracking
        )

    def _ups_rest_get_parcel(self, picking):
        vals = self._roulier_get_parcel(picking)
        vals["number_of_pieces"] = len(self.quant_ids.mapped("quantity"))
        vals["packaging_code"] = "02"  #  custom package TODO make it configurable
        vals[
            "weight_unit"
        ] = "KGS"  #  TODO make it configurable at company level or config param?
        return vals
