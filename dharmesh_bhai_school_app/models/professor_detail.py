from datetime import date
from odoo import models, fields, api


class SchoolProfessor(models.Model):
    _name = 'professor.detail'
    _description = 'school_app.professor'
    _rec_name = 'professor_name'

    professor_name = fields.Char(required=True)
    professor_email = fields.Char()
    professor_mobile = fields.Integer(max_length=10)
    hendler = fields.Integer()
