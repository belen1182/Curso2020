# Copyright 2018
# License AGPL-3.0or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models, _


class HelpdeskTicket(models.Model):
	_name = 'helpdesk.ticket'  # nombre de la tabla de bd (modelo)
	_description = ''

	_inherit = ['mail.thread.cc','mail.activity.mixin']

	name = fields.Char(string='Name', required=True)  # campo de la tabla
	description = fields.Text('Description')
	date_deadline = fields.Datetime('Date Deadline')

	team_id = fields.Many2one(
	comodel_name='helpdesk.team',
	string='Team'
	)

	user_id = fields.Many2many(
	comodel_name='res.users',
	relation='helpdesk_ticket_user_rel',
	column1='ticket_id',
	column2='user_id',
	string='Users'
	)

	responsable_id = fields.Many2one(
	comodel_name='res.users',
	string='Resposable'
	)
	tickets_qty = fields.Integer(
	string='Tickets Qty',
	compute='_compute_tickets_qty'
	)

	@api.depends('responsable_id')
	def _compute_tickets_qty(self):
		ticket_obj = self.env['helpdesk.ticket']
		for ticket in self:
			tickets = ticket_obj.search([
				'|',
				'|',
				('responsable_id','=',ticket.responsable_id.id),
				('responsable_id','=',False),
				('team_id','=',ticket.team_id.id)
			])
			ticket.tickets_qty=len(tickets)


	def set_responsable(self):
		self.ensure_one()
		self.responsable_id = self.env.user

	@api.onchange('name','date_deadline')
	def _onchange_description(self):
		if self.name and self.date_deadline:
			self.description = '%s - %s'%(self.name,self.date_deadline)
		#self.description = self.name + self.date_deadline
