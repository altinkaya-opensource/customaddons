# Copyright 2023 Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.model_create_multi
    def create(self, vals_list):
        """
        Set rate_type context if partner uses custom rate field on Account Move creation
        """
        for vals in vals_list:
            if vals.get("partner_id"):
                partner = self.env["res.partner"].browse(vals["partner_id"])
                if partner and partner.property_rate_field != "rate":
                    self = self.with_context(rate_type=partner.property_rate_field)
        return super(AccountMove, self).create(vals_list)

    # TODO: migration, could be removed in future
    # def action_move_create(self):
    #     new_context = self._context.copy()
    #     if self.partner_id.property_rate_field != "rate" and not self.use_custom_rate:
    #         new_context.update(
    #             {
    #                 "rate_type": self.partner_id.property_rate_field,
    #             }
    #         )
    #     return super(
    #         AccountMove, self.with_context(new_context)
    #     ).action_move_create()
