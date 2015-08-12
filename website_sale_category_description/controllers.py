# -*- coding: utf-8 -*-
from openerp import http

# class WebsiteSaleCategoryDescription(http.Controller):
#     @http.route('/website_sale_category_description/website_sale_category_description/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_sale_category_description/website_sale_category_description/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_sale_category_description.listing', {
#             'root': '/website_sale_category_description/website_sale_category_description',
#             'objects': http.request.env['website_sale_category_description.website_sale_category_description'].search([]),
#         })

#     @http.route('/website_sale_category_description/website_sale_category_description/objects/<model("website_sale_category_description.website_sale_category_description"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_sale_category_description.object', {
#             'object': obj
#         })