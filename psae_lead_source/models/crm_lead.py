from odoo import fields, models


class CrmLead(models.Model)
    _inherit = 'crm.lead'

    source_detail = fields.Char(string="Source Detail")
