from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner_region = fields.Char(string="Region")
