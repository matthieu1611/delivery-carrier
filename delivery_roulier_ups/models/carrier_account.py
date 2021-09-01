# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class CarrierAccount(models.Model):
    _inherit = "carrier.account"

    ups_rest_shipper_number = fields.Char(string="Shipper Number")
    ups_rest_license_number = fields.Char(string="License Number")
    ups_rest_file_format = fields.Selection(
        [
            ("ZPL", "ZPL"),
            ("EPL", "EPL2"),
            ("PNG", "PNG"),
            ("SPL", "SPL"),
            ("GIF", "GIF"),
        ],
        default="ZPL",
        string="File Format",
    )
