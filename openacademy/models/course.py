# -*- coding: utf-8 -*-

from odoo import models, fields

class course(models.Model):
    _name = 'course'
    _description = 'test odoo//python class'

    title = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description", required=False)
    
    omf = fields.Char()
