 #Copyright 2018
# License AGPL-3.0or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models, _


class HelpdeskTeam(models.Model):

    _name ='helpdesk.team'
    _description= 'Team'

    name = fields.Char(
        string='Name',
        required=True)

    ticket_ids = fields.One2many(
        comodel_name='helpdesk.ticket',
        inverse_name='team_id',
        string='Tickets')
