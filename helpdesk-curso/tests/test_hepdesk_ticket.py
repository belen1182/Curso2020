# Copyright 2018
# License AGPL-3.0or later (http://www.gnu.org/licenses/agpl.html)

from odoo.tests import SavepointCase

class TestHelpdeskTicket(SavePointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.team_obj = cls.env["helpdesk.team"]
        cls.ticket_obj = cls.env["helpdesk.ticket"]
        cls.stage_obj = cls.env["helpdesk.stage"]
        cls.users_obj = cls.env["res.users"]

        cls.user_demo=cls.env.ref('base.user_demo')
        ls.user_admin=cls.env.ref('base.user_admin')


    def test_create_ticket(self):
        date='no date'
        ticket_name='test ticket'
        ticket = self.ticket_obj.create({
            'name': ticket_name,
            'responsable_id': self.user_demo.id
        })
        self.assertEqual(ticket.description,'test ticket - no date')

    def test_create_ticket_admin(self):
        ticket = self.ticket_obj.create({
            'name': 'test ticket',
            'responsable_id': self.user_admin.id
        })
