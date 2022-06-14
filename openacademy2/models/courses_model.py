from odoo import models, fields, api


class courses(models.Model):
    _name = 'openacademy2.courses'
    _description = 'Quest 2.3.3'

    title = fields.Char(string = "Title of a course", required = True)
    description = fields.Text(string = "Short course description", required = False)

    responsible = fields.Many2one('res.users', string = "Author/Responsible")

    session = fields.One2many('openacademy2.sessions','course')

    _sql_constraints = [
        (
            'title_is_not_equal_to_desc',
            'CHECK(title!=description)',
            'Enter more specific description'),

        (
           'title_is_unique',
            'UNIQUE(title)',
            'Enter valid unique title'
        )
    ]