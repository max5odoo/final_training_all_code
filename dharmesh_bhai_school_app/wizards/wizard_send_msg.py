from odoo import models, fields, api


class SendMsgWizard(models.TransientModel):
    _name = 'wizard.send_msg'
    _description = 'msg attachment wizard'

    attchment = fields.Binary()
    message_body = fields.Text()

    def send_msg(self):
        student = self.env["student.detail"].browse(
            self._context.get("active_id"))
        print("hi dharmesh")
        attachments = self.env['ir.attachment'].with_user(self.env.user).create({
            'datas': self.attchment,
            'name': student.first_name,
            'res_model': 'mail.compose.message',
        })
        return student.message_post(
            author_id=self.env.ref('base.partner_admin').id,
            body=self.message_body,
            subject="inform you",
            message_type="sms",
            attachment_ids=attachments.ids
        )

    # def message_post(self, *,
    #                  body='', subject=None, message_type='notification',
    #                  email_from=None, author_id=None, parent_id=False,
    #                  subtype_xmlid=None, subtype_id=False, partner_ids=None, channel_ids=None,
    #                  attachments=None, attachment_ids=None,
    #                  add_sign=True, record_name=False,
    #                  **kwargs):
