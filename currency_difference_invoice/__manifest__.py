# -*- coding: utf-8 -*-
{
    'name': "currency_difference_invoice",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        This module:
        * adds main currency of payment in invoice forms widget
        
    """,

    'author': "yibudak",
    'website': "https://github.com/yibudak",
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
    ],
}