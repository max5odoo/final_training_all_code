# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class dharmesh_18_jan_2021(models.Model):
#     _name = 'dharmesh_18_jan_2021.dharmesh_18_jan_2021'
#     _description = 'dharmesh_18_jan_2021.dharmesh_18_jan_2021'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
