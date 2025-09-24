from odoo import models, fields

class MasterPart(models.Model):
    _name = 'master.part'
    _description = 'Master Part'

    name = fields.Char("Part Name", required=True)
    part_number = fields.Char("Part Number", required=True)
    category = fields.Selection(
        [
            ('electrical', 'Electrical'),
            ('mechanical', 'Mechanical'),
            ('hydraulic', 'Hydraulic'),
            ('other', 'Other'),
        ],
        string="Category",
        default='other'
    )
    description = fields.Text("Description")
    cost = fields.Float("Cost")
