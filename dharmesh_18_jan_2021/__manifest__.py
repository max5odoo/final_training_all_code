# -*- coding: utf-8 -*-
{
    'name': "dharmesh_18_jan_2021",

    'summary': """
        help of this app you can check sale orders base on sale order dates,status""",

    'description': """
       The prior purpose for this module is that we can search the records on the basis of the dates and status of that order. 
    """,

    'author': "Dharmesh Jagatiya",
    'website': "http://www.activesoftware.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['sale_management', 'website'],

    # always loaded
    'data': [
        'views/website/website_update.xml',
        'views/website/portal_check_sales_form.xml',
        'views/website/portal_sale_order_list.xml',
        'views/website/portal_sale_order_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
