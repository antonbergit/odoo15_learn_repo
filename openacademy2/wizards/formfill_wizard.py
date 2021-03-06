from odoo import models, fields, api


class formfill(models.TransientModel):
    _name = "openacademy2.formfill"
    _description = "Session and Attendees"

    def default_rel_sessions(self):
        return self.env['openacademy2.sessions'].browse(self._context.get('active_ids'))

    def default_rel_partner(self):
        temp_session = self.env['openacademy2.sessions'].browse(self._context.get('active_ids'))
        if (temp_session):
            return temp_session.attendees

    rel_sessions = fields.Many2many('openacademy2.sessions', string = "Session", default=default_rel_sessions)
    rel_partner = fields.Many2many('res.partner', string = "Attendees", default=default_rel_partner)

    def save_attendees(self):
        for temp_session in self.rel_sessions:
            temp_session.attendees = False
            for temp_attendee in self.rel_partner:
                temp_session.attendees |= temp_attendee