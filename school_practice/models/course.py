import simplejson

from odoo import api, fields, models
from lxml import etree
from odoo.tools.safe_eval import json


class Course(models.Model):
    _name = 'course.details'
    _description = 'This is the course class'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'course_name'

    course_name = fields.Char()
    amount = fields.Integer()
    duration = fields.Integer()
    is_active = fields.Boolean(default=True)
    price_tax = fields.Float(string='Total Tax')

    #
    # def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
    #     res = super(Course, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
    #                                               submenu=submenu)
    #     print(f'\n\n\n\nfields_get_view-->callable\n\n\n\n')
    #     print(f'\n\n\n\nfields_get_view-->value{res}\n\n\n\n')
    #     print(f'\n\n\n\ncontext-->value{self.env.context}\n\n\n\n')
    #     print(f'\n\n\n\ncontext new-->value{self._context}\n\n\n\n')
    #     # if self.env.context.get('the_context'):  # Check for context value
    #     #     print(f'\n\n\n\ncontext-->callable INSIDE\n\n\n\n')
    #     #     doc = etree.XML(res['arch'])
    #     #     print(f'\n\n\n\ndoc-->value\n\n\n\n')
    #     #     print(f'\n\n\n\ndoc-->value\n\n\n\n')
    #
    #     if self.browse(self.env.context.get('the_context')).is_active == (str(True)) :
    #         doc = etree.XML(res['arch'])
    #         print(f'\n\n\n\nform-->value\n\n\n\n')
    #         try:
    #             for node in doc.xpath("//field"):  # All the view fields to readonly
    #                 node.set('readonly', "1")
    #                 modifiers = json.loads(node.get("modifiers"))
    #                 modifiers['readonly'] = True
    #                 node.set("modifiers", json.dumps(modifiers))
    #                 res['arch'] = etree.tostring(doc)
    #         except:
    #
    #          return res

    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        res = super(Course, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
                                                  submenu=submenu)
        print(f'\n\n\n\ncontext-->value{self.env.context}\n\n\n\n')
        if self.env.context.get('new_context'):
            print(f'\n\n\n\nform-->value\n\n\n\n')
            doc = etree.XML(res['arch'])
            if view_type == 'form':
                for node in doc.xpath("//field"):
                    modifiers = simplejson.loads(node.get("modifiers"))
                    node.set('modifiers',
                             simplejson.dumps(modifiers))
                res['arch'] = etree.tostring(doc)
        return res
