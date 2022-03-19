# -*- coding: utf-8 -*-
# from odoo import http


# class Reporteador(http.Controller):
#     @http.route('/reporteador/reporteador/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reporteador/reporteador/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('reporteador.listing', {
#             'root': '/reporteador/reporteador',
#             'objects': http.request.env['reporteador.reporteador'].search([]),
#         })

#     @http.route('/reporteador/reporteador/objects/<model("reporteador.reporteador"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reporteador.object', {
#             'object': obj
#         })
