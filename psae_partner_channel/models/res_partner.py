from odoo import fields, models


class ResPartner(models.Model)
    _inherit = 'res.partner'

    sales_channel = fields.Char(string="Sales Channel")
