from datetime import date
from odoo import models, fields, api


class SchoolCourse(models.Model):
    _name = 'course.detail'
    _description = 'school_app.courses'
    _rec_name = 'course_name'

    course_name = fields.Char(string='Course name', required=True)
    course_amount = fields.Float(digits=(4, 2))
    course_length = fields.Integer(max_length=10)
    course_duration = fields.Integer()
    course_active = fields.Boolean(default=True)
    hendler = fields.Integer()
    color = fields.Integer()
