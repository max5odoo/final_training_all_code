# -*- coding: utf-8 -*-
# from odoo import http


# class Dharmesh18Jan2021(http.Controller):
#     @http.route('/dharmesh_18_jan_2021/dharmesh_18_jan_2021/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dharmesh_18_jan_2021/dharmesh_18_jan_2021/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dharmesh_18_jan_2021.listing', {
#             'root': '/dharmesh_18_jan_2021/dharmesh_18_jan_2021',
#             'objects': http.request.env['dharmesh_18_jan_2021.dharmesh_18_jan_2021'].search([]),
#         })

#     @http.route('/dharmesh_18_jan_2021/dharmesh_18_jan_2021/objects/<model("dharmesh_18_jan_2021.dharmesh_18_jan_2021"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dharmesh_18_jan_2021.object', {
#             'object': obj
#         })
