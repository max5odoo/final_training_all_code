# -*- coding: utf-8 -*-
{
    'name': "school_app",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        school module help's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.2.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'sale_management', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',


        # --------------wizards-----------------
        'wizards/wizard_send_msg.xml',

        # --------------school app views--------
        # 'views/templates.xml',
        'views/course_detail.xml',
        'views/professor_detail.xml',
        'views/student_detail.xml',
        'views/action_button.xml',
        'views/product_cataloge.xml',

        # --------------website-----------------
        'views/website/school_list_view.xml',
        'views/website/add_student_views.xml',



        # --------------inherits-----------------
        'inherits/inherit_sale.xml',
        'inherits/but_addon_action_sale.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'auto_install': True,
    'installation': True
}
