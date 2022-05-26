from odoo import models, fields, api


class courses(models.Model):
    _name = 'openacademy2.courses'
    _description = 'Quest 2.3.3'

    title = fields.Char(string = "Title of a course", required = True)
    description = fields.Text(string = "Short course description", required = False)

    responsible = fields.Many2one('res.users', string = "Author/Responsible")

    session = fields.One2many('openacademy2.sessions','course')
