from odoo import models, fields, api


class sessions(models.Model):
    _name = 'openacademy2.sessions'
    _description = 'Quest 2.3.7'

    name = fields.Char(string = "Session ident name")
    start_date = fields.Date(string = "First day", default=fields.Date.today())
    duration = fields.Integer(string = "Duration on weeks")
    seats = fields.Integer(string = "Number of seats")
    seats_reserved = fields.Float(compute = '_seats_reserved')
    active = fields.Boolean(default=True)

    instructor = fields.Many2one('res.partner', string = "Instructor/Trainer")
    course = fields.Many2one('openacademy2.courses', required = False, string = "Course id")
    attendees = fields.Many2many('res.partner', string = "Attendees")



    @api.depends('seats','attendees')
    def _seats_reserved(self):
        for rec_session in self:
            if (rec_session.seats != 0):
                rec_session.seats_reserved = 100 * len(rec_session.attendees) / rec_session.seats
            else:
                rec_session.seats_reserved = 0.0

    @api.onchange('seats','attendees')
    def _seats_reserve_check(self):
        if (self.seats <= 0):
            return {
                'warning': {
                    'title': "Seats enter exception",
                    'message': "A number of seats must be a positive value"
                }
            }
        if (len(self.attendees)>self.seats):
            return {
                'warning': {
                    'title': "Attendees enter exception",
                    'message': "A number of attendees can not be more then seats count"
                }
            }
