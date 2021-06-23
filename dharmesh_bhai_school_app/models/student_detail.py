from datetime import date
from odoo import models, fields, api, _
from os.path import join, dirname
from odoo.tools.misc import xlsxwriter
from datetime import date, timedelta
from lxml import etree
try:
    import xlrd
    try:
        from xlrd import xlsx
    except ImportError:
        xlsx = None
except ImportError:
    xlrd = xlsx = None


class SchoolStudent(models.Model):
    _name = 'student.detail'
    _description = 'school_app.student'
    _rec_name = 'first_name'
    _inherit = ['mail.thread',
                'mail.activity.mixin']
    _sql_constraints = [
        ('age_constrain',
         'CHECK(age>18)',  # age above 18 = True else false
         'enter your age above 18'),

    ]

    active = fields.Boolean()
    profile_pic = fields.Binary()
    first_name = fields.Char(string='First name', required=True)
    last_name = fields.Char()
    email = fields.Char()
    age = fields.Integer(string='Age')
    dob = fields.Date()
    mobile_no = fields.Integer(max_length=10)
    address = fields.Text()
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirm', 'Confirm'),
         ('paid', 'Paid'),
         ('cancel', 'Cancel')])
    hendler = fields.Integer()
    course_ids = fields.Many2many(
        "course.detail", "stu_course_rel", "stu_id", "course_id")
    courses_count = fields.Integer(compute='Course_counts')
    professor_count = fields.Integer(compute='professor_counts')
    sal = fields.Many2one('sale.order')
    f_view_field = fields.Integer()

    # def name_get(self):
    #     print(f"\n\n\nnem get{self}\n\n\n")
    #     result = []
    #     for rec in self:
    #         if rec.first_name and rec.last_name:
    #             name = f"{rec.first_name} {rec.last_name}"
    #         else:
    #             name = f"{rec.first_name}"
    #         result.append((rec.id, name))
    #         print(f"\n\n\n{result}\n\n\n")
    #     return result

    def default_get(self, field_list=[]):
        # print(f"\n\n\n\ninput{field_list}\n\n\n\n")
        rtn = super(SchoolStudent, self).default_get(field_list)
        rtn['first_name'] = 'odoo'
        rtn['last_name'] = 'bot'
        rtn['email'] = 'dharmesh_ja@gmail.com'
        rtn['active'] = True
        rtn['first_name'] = 'samplename'
        rtn['gender'] = 'male'
        # print(f"\n\n\n\nertun data{rtn}\n\n\n\n")
        return rtn

    def copy(self):
        # print(f"\n\n\n{default}\n\n\n\n")
        # default = dict(default or {})
        # default['first_name'] = _("%s", self.first_name)
        # default['last_name'] = ''
        rtn = super(SchoolStudent, self).copy()
        print(f"\n\n\n{rtn}\n\n\n\n")
        return rtn

    def name_get(self):
        # print(f"{self.env.context}")
        result = []
        for rec in self:
            sale_name_str = rec.first_name
            if not self.env.context.get('sale_name'):
                sale_name_str = f"{rec.first_name} {rec.last_name}"

            result.append((rec.id, sale_name_str))
            print(f"\n\n\nname get{result}\n\n\n")
        return result

    def fields_view_get(self, view_id=None, view_type='form', toolbar=False,
                        submenu=False):

        result = super(SchoolStudent, self).fields_view_get(view_id=view_id,
                                                            view_type=view_type,

                                                            toolbar=toolbar,
                                                            submenu=submenu)
        if view_type == 'form':

            # active_id = context.get('dharmesh')

            print(
                f"\n\n\n\n\nhi field_view_get Callllll-2{fields}\n\n\n\n\n\n\n")

        return result

    @ api.model
    def name_create(self, name):
        # first way
        # rtn = super(SchoolStudent, self).name_create(name)
        # second way
        rtn = self.creat({"first_name": name, "last_name": ''})
        rtn.namme_get()[0]
        # print(f"\n\n\nname_get\n{rtn}\n\n\n\n")
        return rtn
    # ---------------------ORM--------------------------------

    @ api.model
    def create(self, vals):
        print("\n\n\ncreate mathod is call\n")
        rtn = super(SchoolStudent, self).create(vals)
        print(rtn)
        return rtn

    def write(self, vals):
        print("\n\n\nwrite mathod is call\n")
        rtn = super(SchoolStudent, self).write(vals)
        print(rtn)
        return rtn

    def unlink(self):
        print("\n\n\nunlink mathod is call\n")
        print(self)
        rtn = super(SchoolStudent, self).unlink()
        print(rtn)
        return rtn
    # ----------------------------------------------------------

    def Course_counts(self):
        for rec in self:
            cour_count = self.env['course.detail'].search_count([])
            rec.courses_count = cour_count

    def professor_counts(self):
        prof_count = self.env['professor.detail'].search_count([])
        self.write({'professor_count': prof_count})

    def professor_view(self):
        print(f"\n\n\nhi profesoor\n\n\n")
        return {
            'name': "professor",
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'professor.detail',
            # 'view_id': self.env.ref('school_app.school_professor_tree_view').id,
            # 'context': ctx,
        }

    def confirm_state(self):
        print("confrim")
        self.write({'state': 'confirm'})

    def draft_state(self):
        print("draft")
        self.write({'state': 'draft'})

    def paid_state(self):
        print("draft")
        self.write({'state': 'paid'})

    def cancel_state(self):
        print("draft")
        self.write({'state': 'cancel'})

    @ api.onchange('dob')
    def calc_age(self):
        for rec in self:
            if rec.dob:
                your_date = rec.dob
                today_date = date.today()
                rec.age = abs(((today_date - your_date) // 365).days)
                # self.write({'state': 'cancel'})

                # form scedule activity create advance date generate
                # print(f"\n\n\n{rec.dob + timedelta(days=1)}\n\n\n\n")

    def read_report(self):
        wb = xlrd.open_workbook(
            "D:/odoo job/odoo/custom_addons/student_record.xls")
        sheet_name = wb.sheet_by_name('jagatiya')
        val_firstname1 = sheet_name.cell_value(1, 0)
        val_lastname1 = sheet_name.cell_value(1, 1)
        val_age1 = sheet_name.cell_value(1, 2)
        # print(f"\n\n\n\n{val_firstname1}, {val_lastname1}, {val_age1}\n\n\n\n")
        # print(dir(wb))

    def write_report(self):
        students = self.env["student.detail"].search([])
        # filename = f"D:/odoo job/odoo/custom_addons/{self.first_name}.xls"
        filename = "D:/odoo job/odoo/custom_addons/school_app/static/xls/student_rec.xls"
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet(self.first_name)
        header_bold = workbook.add_format(
            {'bold': True, 'pattern': 1, 'bg_color': '#AAAAAA'})
        worksheet.write(0, 0, 'Name', header_bold)
        worksheet.write(0, 1, 'Surname', header_bold)
        worksheet.write(0, 2, 'Age', header_bold)
        rows = 1

        for student in students:
            worksheet.write(rows, 0, student.first_name)
            worksheet.write(rows, 1, student.last_name)
            worksheet.write(rows, 2, student.age)
            rows += 1
        workbook.close()

    # @api.constrains('email')
    # def _validate_email(self):
    #     self.email.replace(" ", "") if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
    #         raise exceptions.ValidationError(
    #             "Please enter valid email address")
