from odoo import models, fields, api


class sessions(models.Model):
    _name = 'openacademy2.sessions'
    _description = 'Quest 2.3.7'

    name = fields.Char(string = "Session ident name")
    start_date = fields.Date(string = "Firs day")
    duration = fields.Integer(string = "Duration on weeks")
    seats = fields.Integer(string = "Number of seats")

    instructor = fields.Many2one('res.partner', string = "Instructor/Trainer")
    course = fields.Many2one('openacademy2.courses', required = False, string = "Course id")
    attendees = fields.Many2many('res.partner', string = "Attendees")
