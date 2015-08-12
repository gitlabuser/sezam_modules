# -*- coding: utf-8 -*-
{
    'name': "website_sale_category_description",

    'summary': """
        Show a full description of product category on ecommerce website when displaying a category""",

    'description': """
        Long description of module's purpose
    """,

    'author': "SEZAM",
    'website': "http://www.sezam.eu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}