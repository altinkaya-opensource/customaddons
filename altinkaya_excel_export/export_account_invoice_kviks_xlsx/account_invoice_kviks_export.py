# Copyright 2019 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import fields, models, api


class ReportAccountMoveKVIKS(models.TransientModel):
    _name = 'report.account.move.kviks'
    _description = 'Wizard for report.account.invoice.kviks'
    _inherit = 'xlsx.report'

    # Report Result, account.invoice
    results = fields.Many2many(
        comodel_name='account.move',
        string='Invoices',
        compute='_get_invoices',
        help='Use compute fields, so there is nothing stored in database',
    )

    
    def _get_invoices(self):
        selected_ids = self.env.context.get('active_ids', [])
        ids = self.env['account.move'].browse(selected_ids)
        for rec in self:
            rec.results = ids
