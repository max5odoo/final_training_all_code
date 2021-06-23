from odoo.http import request
from odoo.http import route, Controller


class PortalUpdate(Controller):
    @route(['/my/check_order'], type='http', auth='user', website=True)
    def check_sale_order(self, redirect=None, **post):
        domain = []
        values = {}

        if request.httprequest.method == 'POST':
            start_date = post['start_date']
            end_nate = post['end_date']
            status = post['status']
            domain = [('date_order', '>=', start_date),
                      ('date_order', '<=', end_nate)]
            if status != 'all':
                domain += [('state', '=', status)]
            orders = request.env['sale.order'].sudo().search(domain)
            request.session.od_count = len(orders)
            values.update({

                'orders': orders,

            })

            return request.render('dharmesh_18_jan_2021.portal_order_view', {'orders': orders})
        return request.render('dharmesh_18_jan_2021.check_sale_order')

    @route(['''/my/check_order/<int:order_id>'''
            ], type='http', auth="user", website=True)
    def sale_order_view(self, order_id=None, **post):
        values = {}
        so_ref = request.env['sale.order'].sudo().browse([order_id])
        return request.render('dharmesh_18_jan_2021.portal_sale_order_view', {'so_ref': so_ref})
