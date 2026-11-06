from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    credit_rating = fields.Char(string="Credit Rating")
