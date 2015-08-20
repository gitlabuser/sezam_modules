# -*- coding: utf-8 -*-
from openerp import http

# class WebsiteSaleShowUos(http.Controller):
#     @http.route('/website_sale_show_uos/website_sale_show_uos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_sale_show_uos/website_sale_show_uos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_sale_show_uos.listing', {
#             'root': '/website_sale_show_uos/website_sale_show_uos',
#             'objects': http.request.env['website_sale_show_uos.website_sale_show_uos'].search([]),
#         })

#     @http.route('/website_sale_show_uos/website_sale_show_uos/objects/<model("website_sale_show_uos.website_sale_show_uos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_sale_show_uos.object', {
#             'object': obj
#         })