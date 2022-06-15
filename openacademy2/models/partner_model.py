from odoo import models, fields, api


class partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    instructor = fields.Boolean(string = 'I am instructor')
    teacher = fields.Selection(
                                [('l1','Level 1'),
                                 ('l2','Level 2')]
        ,string="Teacher level")

    session = fields.Many2many('openacademy2.sessions')