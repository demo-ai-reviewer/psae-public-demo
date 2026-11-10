from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    loyalty_level = fields.Char(string="Loyalty Level")
