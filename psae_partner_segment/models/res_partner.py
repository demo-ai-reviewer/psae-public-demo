from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_segment = fields.Selection(
        selection=[
            ('retail', "Retail"),
            ('wholesale', "Wholesale"),
            ('distributor', "Distributor"),
        ],
        string="Customer Segment",
    )
