# -*- coding: utf-8 -*-

from odoo import models, fields

class Report(models.Model):
    _name = 'reporteador.report'
    _description = 'Report'
    _order = 'fecha_reporte desc'

    titulo = fields.Char(string = 'Título', help = 'Introduce un par de palabras que expresen o que ocorre.', required = True)
    descripcion = fields.Text(string = 'Descripción', help = 'Introduce unha descripción do erro.', required = True)
    fecha_reporte = fields.Datetime(string = 'Fecha do erro', help = 'Selecciona a fecha do erro.', required = True)
    fecha_solucionado = fields.Datetime(string = 'Fecha da arreglo', help = 'Selecciona a fecha na que solucionou o erro')
    empleados_ids = fields.Many2many('res.partner', string='Empregados')
    cliente_id = fields.Many2one('res.partner', string = 'Cliente')