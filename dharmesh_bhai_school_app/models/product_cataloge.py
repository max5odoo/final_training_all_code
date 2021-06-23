from datetime import date
from odoo import models, fields, api
from odoo.osv import expression


class ProductCataloge(models.Model):
    _name = 'product.calaloge'
    _description = 'school_app.product'
    _rec_name = "product_name"

    product_name = fields.Char()
    product_line_ids = fields.One2many(
        "product.calaloge.lines", 'product_cat_id')


class ProductCatalogeLines(models.Model):
    _name = 'product.calaloge.lines'
    _description = 'school_app.courses'
    _rec_name = 'name'

    name = fields.Char()
    product_cat_id = fields.Many2one("product.calaloge")
    disc = fields.Text()

    # def name_get(self):
    #     print(f"\n\n\nnem get{self}\n\n\n")
    #     result = []
    #     for rec in self:
    #         if rec.product_cat_id.product_name:
    #             name = f"{rec.product_cat_id.product_name}"

    #     result.append((rec.id, name))
    #     print(f"\n\n\nname_get ====>{result}\n\n\n")
    #     return result

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, ):
        print(f"\n\n\n\nabc======>{name}\n\n\n\n")

        args = args or []
        domain = []
        context = self._context

        if context.get('cataloge_name'):

            domain = [('product_cat_id', "=", context.get("cataloge_name"))
                      ]
        return self._search(expression.AND([domain, args]))
