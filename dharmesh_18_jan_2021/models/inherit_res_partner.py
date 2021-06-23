from odoo import models, fields, api
from odoo.osv import expression


class InheritRespatner(models.Model):
    _inherit = 'res.partner'
    _description = 'dharmesh_18_jan_2021.dharmesh_18_jan_2021'

    check_field = fields.Char()

    def name_get(self):
        print(f"\n\n\nnem get{self}\n\n\n")
        result = []
        for rec in self:
            if rec.name and rec.city:
                name = f"{rec.name} ({rec.city})"
            else:
                name = f"{rec.name}"
            result.append((rec.id, name))
            print(f"\n\n\n{result}\n\n\n")
        return result

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, ):
        args = args or []
        domain = []
        domain = args+[('city', "ilike", name)
                       ]
        return self._search(expression.AND([domain, args]))
