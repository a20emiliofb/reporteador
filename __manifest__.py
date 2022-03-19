# -*- coding: utf-8 -*-
{
    'name': "Reporteador",

    'summary': """
        Módulo que sirve para xestionar os reportes.
        """,

    'description': """
        Con este módulo poderás engadir novos reportes. Estes
        podes asocialos a un traballador. E estes poderán solucionalos.
    """,

    'author': "Emilio Fajín Bargo",
    'website': "https://github.com/a20emiliofb",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '14.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
