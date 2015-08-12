# -*- coding: utf-8 -*-

from openerp import models, fields, api

class website_sale_category_description(models.Model):
    _inherit = 'product.public.category'

    description = fields.Html()
#    name = fields.Char()