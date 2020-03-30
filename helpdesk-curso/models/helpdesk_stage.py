 #Copyright 2018
# License AGPL-3.0or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models, _


class HelpdeskStage(models.Model):

    _name = 'helpdesk.stage'
    _description = 'Helpdesk Stage'

    stage = fields.Char(string='stage', required=True)
