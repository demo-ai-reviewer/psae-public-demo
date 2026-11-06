from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_ref_code = fields.Char(
        string="Customer Reference Code",
        help="Reference the customer uses for this contact in their own system.",
    )
