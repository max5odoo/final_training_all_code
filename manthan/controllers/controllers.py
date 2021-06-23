# -*- coding: utf-8 -*-
# from odoo import http


# class Manthan(http.Controller):
#     @http.route('/manthan/manthan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manthan/manthan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('manthan.listing', {
#             'root': '/manthan/manthan',
#             'objects': http.request.env['manthan.manthan'].search([]),
#         })

#     @http.route('/manthan/manthan/objects/<model("manthan.manthan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manthan.object', {
#             'object': obj
#         })
