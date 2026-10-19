from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    delivery_note = fields.Text(help="Instructions for the carrier, printed on the delivery slip.")
    delivery_note_required = fields.Boolean(compute="_compute_delivery_note_required")

    def _compute_delivery_note_required(self):
        for order in self:
            order.delivery_note_required = order.partner_id.country_id != order.company_id.country_id
