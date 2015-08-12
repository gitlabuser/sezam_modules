# -*- coding: utf-8 -*-
from openerp import http

# class ChangeFavicon(http.Controller):
#     @http.route('/change_favicon/change_favicon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/change_favicon/change_favicon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('change_favicon.listing', {
#             'root': '/change_favicon/change_favicon',
#             'objects': http.request.env['change_favicon.change_favicon'].search([]),
#         })

#     @http.route('/change_favicon/change_favicon/objects/<model("change_favicon.change_favicon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('change_favicon.object', {
#             'object': obj
#         })