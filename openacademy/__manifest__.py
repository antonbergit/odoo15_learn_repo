# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Open Academy project for beginners""",

    'description': """
        Just another one study project for ODOO15
    """,

    'author': "BRGM",
    'website': "",
    'license': "LGPL-3",
    'version': '1.0.0',
    'sequence': -100,
    # any module necessary for this one to work correctly
    'depends': [],
    'category': "Administration",
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml'
    ],
}
