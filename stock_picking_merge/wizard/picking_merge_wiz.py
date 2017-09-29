# coding: utf-8

from openerp.exceptions import Warning as UserError
from openerp import api, fields, models, _


class StockPickingMerge(models.TransientModel):
    _name = 'stock.picking.merge'
    _description = 'Merge Pickings'

    destination_picking_id = fields.Many2one('stock.picking', string="Destination Picking")
    source_picking_ids = fields.Many2many('stock.picking', 'picking_merge_rel', 'merge_id', 'picking_id', string="Source Picklings")

    @api.onchange('destination_picking_id')
    def onchange_destination_picking_id(self):
        res = {'domain': []}
        if self.env.context.get('active_domain'):
            for picking_type in self.env.context.get('active_domain'):
                if picking_type[0] == 'picking_type_id':
                    res.update({'domain': {'destination_picking_id': [('picking_type_id', '=', picking_type[2]), ('state','not in',['done','cancel'])]}})
        return res

    @api.model
    def default_get(self, fields):
        ''' 
        To get default values for the object.
        '''
        res = super(StockPickingMerge, self).default_get(fields)
        res.update({'source_picking_ids': [(6, 0, self.env.context.get('active_ids'))] or []})
        return res

    @api.multi
    def merge_picking(self):
        move_obj = self.env['stock.move']
        if self.destination_picking_id.id in self.source_picking_ids.ids:
             raise UserError(_('Destination Picking must be not in list of pickings!'))
        picking_ids = [picking for picking in self.source_picking_ids if picking.partner_id.id == self.destination_picking_id.partner_id.id and picking.picking_type_id.id == self.destination_picking_id.picking_type_id.id and picking.location_id.id == self.destination_picking_id.location_id.id and picking.location_dest_id.id == self.destination_picking_id.location_dest_id.id and picking.invoice_state == self.destination_picking_id.invoice_state and picking.company_id.id == self.destination_picking_id.company_id.id and picking.state not in ['done','cancel']]
        for picking in picking_ids:
            for move in picking.move_lines:
                move.copy(default={'picking_id': self.destination_picking_id.id})
            for pack_operation in picking.pack_operation_ids:
                pack_operation.copy(default={'picking_id': self.destination_picking_id.id})
            if picking.note:
                self.destination_picking_id.note += "\n\n" + picking.note
            if picking.origin:
                self.destination_picking_id.origin += "," + picking.origin
            attachments = self.env['ir.attachment'].search([('res_model','=',picking._name), ('res_id','=',picking.id)])
            for attachment in attachments:
                attachment.copy(default={'res_id': self.destination_picking_id.id, 'res_name': self.destination_picking_id.name})
            picking.action_cancel()
        return True