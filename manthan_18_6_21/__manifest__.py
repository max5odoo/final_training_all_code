# -*- coding: utf-8 -*-
{
    "name": "manthan_18_6_21",
    "summary": """
       This is the module for checking the sale records between  two dates.""",
    "description": """
       The prior purpose of this module is that we can have the  records on the basis of provided date and also states.
    """,
    "author": "My Company",
    "website": "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "14.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["sale_management", "website"],
    # always loaded
    "data": [
        "views/portal_layout.xml",
        "views/sale_order_detail_template.xml",
        "views/list_sale_order_show.xml",
    ],
}
