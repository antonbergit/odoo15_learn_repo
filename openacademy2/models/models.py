# -*- coding: utf-8 -*-

from odoo import models, fields, api


class courses(models.Model):
    _name = 'openacademy2.courses'
    _description = 'Quest 2.3.3'

    title = fields.Char(string = "Title of a course", required = True)
    description = fields.Text(string = "Short course description", required = False)

    responsible = fields.Many2one('res.users', string = "Author/Responsible")

    session = fields.One2many('openacademy2.sessions','course')


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

class partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    instructor = fields.Boolean(stirng = 'I am instructor')
    session = fields.Many2many('openacademy2.sessions')