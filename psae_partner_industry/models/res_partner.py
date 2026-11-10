from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner_industry = fields.Char(string="Industry")
