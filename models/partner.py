# -*- coding: utf-8 -*-

from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    is_employee = fields.Boolean(string='Empregado')
    is_client = fields.Boolean(string='Cliente')
    solved_reports_ids = fields.Many2many('reporteador.report', string = 'Reportes solucionados')
    reported_reports_ids = fields.One2many('reporteador.report', 'cliente_id', string = 'Reportes feitos')