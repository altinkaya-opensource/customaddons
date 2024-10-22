# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountIncoterms(models.Model):
    _inherit = 'account.incoterms'

    destination_port = fields.Boolean(string="Requires destination port")
    transport_type = fields.Boolean(string="Requires transport type")

    # def name_get2(self, cr, uid, ids, context=None):
    #     res = []
    #     for inst in self.browse(cr, uid, ids, context=context):
    #         name='['+inst.code+']'+inst.name
    #         res.append((inst.id, name))
    #     return res
    #
    # @api.model
    # def name_search(self, name, args=None, operator='ilike', limit=80):
    #     if args is None:
    #         args = []
    #
    #     if name:
    #         args += [('name', operator, name)]
    #     ids = self.search(args, limit=limit)
    #     return [inc.code]