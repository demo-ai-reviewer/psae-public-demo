from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_tier = fields.Char(string="Customer Tier")
