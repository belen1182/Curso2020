# Copyright 2018
# License AGPL-3.0or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models, _

class DisplacementTravel(models.Model):
    _name = 'displacement.travel'
    _description = 'Se van a almacenar los desplazamientos de los empleados'

    name = fields.Char(string='Name', required=True)
    description = fields.Text('Description')
    date_start = fields.Datetime('Start Date')
    date_end = fields.Datetime('End Date')
