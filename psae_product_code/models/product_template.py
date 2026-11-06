from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    supplier_code = fields.Char(string="Supplier Code")
