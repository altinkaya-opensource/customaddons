# -*- coding: utf-8 -*-
{
    'name': "Cron Failure Notification",
    'version': '13.0.1.0.1',
    'category': 'Extra Tools',
    'summary': """Cron jobs/Scheduled Actions failure Log Notification & Its PDF Reports""",
    'description': """
        This module will generate error Logs for Scheduled
        Actions / Cron jobs running in backend server
    """,
    'author': "app-script",
    'company': "App Script",
    'website': "http://www.app-script.com",
    'depends': ['base', 'mail', 'web', 'base_setup'],
    'data': [
        'views/logs_scheduled_actions_view.xml',
        'views/error_log_report_template.xml',
        'views/report.xml',
        'views/error_mail_template.xml',
        'security/ir.model.access.csv',
        'demo/ir_cron_demo.xml'
    ],
    'demo': [
        'demo/ir_cron_demo.xml'
    ],
    'images': [
        'static/description/banner.png'
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
