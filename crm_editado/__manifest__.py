# -*- coding: utf-8 -*-
{
    'name': "CRM Test1",

    'summary': """Modificaciones del  CRM""",

    'description': """
        modificando crm
    """,

    'author': "soluciones4g",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_crm'],

    # always loaded
    'data': [
        'views/vista_crm.xml',
        'views/vista_partner.xml',
        'views/vista_saleOrder.xml',
        'views/vista_encuesta.xml',
        #'views/vista_reunion.xml',
        #'views/vista_partner_corrigiendo.xml',
        #'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo_curso.xml',
    ],
    'intallable': True,
    'auto_install': False,
}
