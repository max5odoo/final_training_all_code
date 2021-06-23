from odoo import models, fields, api
from datetime import date, timedelta


class schoolSaleInherit(models.Model):
    _inherit = "sale.order"

    genders = [('male', 'Male'),
               ('female', 'Female'),
               ('other', 'Other')]

    is_active = fields.Boolean(default=True)
    student_id = fields.Many2one('student.detail')
    gender = fields.Selection(genders)
    courses_count = fields.Integer(compute='Course_count', store=True)
    age = fields.Integer()
    products_id = fields.Many2one("product.calaloge")
    rel_search = fields.Char()

    def Course_count(self):
        cour_count = self.env['course.detail'].search_count([])
        self.write({'courses_count': cour_count})

    # @api.depends("student_id.dob")
    # def calc_age(self):
    #     for rec in self:
    #         rec.age = 0
    #         if rec.student_id.dob:
    #             print(
    #                 f"\n\n\nsale order{((date.today() - rec.student_id.dob).days)//365}\n\n\n\n")
    #             cal_age = ((date.today() - rec.student_id.dob).days)//365
    #             rec.write({'age': cal_age})


class schoolSaleInherit(models.Model):
    _inherit = "sale.order.line"

    hi = fields.Char()
    procat_line_ids = fields.Many2one('product.calaloge.lines',)
    sale_order_line_ids = fields.Many2one('sale.order.lines')
