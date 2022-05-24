# -*- coding: utf-8 -*-
{
    'name': "openacademy2",

    'summary': """
        Next lap to try""",

    'description': """
        ODOO study, Python learn
    """,

    'author': "ABI-BRGm",
    #'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'sequence': '-1000',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml'
    ],
}
