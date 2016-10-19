# coding: utf-8
# @author Raphael Reverdy <raphael.reverdy@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Delivery Carrier Roulier',
    'version': '0.3',
    'author': 'Akretion',
    'summary': 'Integration of multiple carriers (base)',
    'maintainer': 'Akretion',
    'category': 'Warehouse',
    'depends': [
        'partner_helper',
        'base_phone',
        'document',
        'delivery_carrier_b2c',
    ],
    'description': "",
    'website': 'http://www.akretion.com/',
    'data': [
        'data/delivery.xml',
        # 'stock_view.xml',
    ],
    'demo': [
    ],
    'external_dependencies': {
        'python': [
            'roulier',  # 'git+https://github.com/akretion/roulier.git'
        ],
    },
    'tests': [],
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
    'application': False,
}
