from odoo import http
from odoo.http import request
import json


class SchoolajaxApp(http.Controller):
    @http.route('/school_app', auth='public', type='http', website=True)
    def school_index(self, **kw):
        return http.request.render('school_app.school_list_view')

    @http.route('/school_app/get_data', auth='public', type='http', website=True)
    def school_data(self, **kw):
        students_rec = request.env['student.detail'].sudo().search([])

        students = []

        for student_rec in students_rec:
            vals = {
                'id': student_rec.id,
                'first_name': student_rec.first_name,
                'last_name': student_rec.last_name,
                'gender': student_rec.gender,
                'mobile_no': student_rec.mobile_no,
                'email_id': student_rec.email
            }
            students.append(vals)

        print(f"\n\n\n students rec :  {students_rec} \n\n\n ")
        print(f"\n\n\n students rec :  {students} \n\n\n ")

        return json.dumps({'students': students})

    @http.route('/add-student', auth='public', type='http', website=True)
    def add_school_index(self, **kw):

        return http.request.render('school_app.add_student_views')

    @http.route('/add-student-ajax', auth='public', type='http', website=True)
    def add_school_ajax(self, **kw):
        if request.httprequest.method == 'POST':
            print("\n\n\n post method called... \n\n\n")
            # create student rec
            new_student = request.env['student.detail'].create(kw)
            if new_student:
                return json.dumps({'message': 'new student created successfully...'})
            else:
                return json.dumps({'message': 'something went wrong...'})
