#Copyright 2018
#License AGPL-3.0or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models, _


class HelpdeskTicket(models.Model):
	_name = 'helpdesk.ticket'  # nombre de la tabla de bd (modelo)
	name = fields.Char(string='Name', required=True)  # campo de la tabla
	description = fields.Text('Description')
	date_deadline = fields.Datetime('Date limit')
