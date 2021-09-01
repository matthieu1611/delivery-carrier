# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Delivery Carrier UPS",
    "version": "14.0.1.0.1",
    "summary": "Generate Label for UPS",
    "author": "Akretion,Odoo Community Association (OCA)",
    "maintainers": ["florian-dacosta"],
    "website": "https://github.com/OCA/delivery-carrier",
    "category": "Warehouse",
    "excludes": ["delivery_ups", "delivery_ups_oca"],
    "depends": [
        "delivery_roulier",
    ],
    "data": [
        "data/delivery.xml",
        "views/carrier_account_views.xml",
    ],
    "installable": True,
    "license": "AGPL-3",
}
