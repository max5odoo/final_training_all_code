from odoo import http, _
from odoo.http import request, route
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager


# class SaleRoute(http.Controller):
#     @http.route("/register/sale/prac", type="http", auth="public", website=True)
#     def sale_registration(self):
#         return http.request.render("manthan_18_6_21.sale_order_front")


class FinalSaleRoute(http.Controller):
    @http.route("/salefront/form/submit", type="http", auth="public", website=True)
    def sale_post_data(self, **post):
        my_method = 'none'
        if request.httprequest.method == 'POST':
            my_method = 'post'
            end_date_data = post["end_date"]
            start_date_data = post["start_date"]
            state_data = post["state"]
            print("state_data", state_data)
            if state_data == "all":
                sale_details = (
                    request.env["sale.order"]
                        .sudo()
                        .search(
                        [
                            ("date_order", ">=", start_date_data),
                            ("date_order", "<=", end_date_data),
                        ]
                    )
                )
            else:
                sale_details = (
                    request.env["sale.order"]
                        .sudo()
                        .search(
                        [
                            ("date_order", ">=", start_date_data),
                            ("date_order", "<=", end_date_data),
                            ("state", "=", state_data),
                        ]
                    )
                )
            vals = {
                "sale_details": sale_details,
                'my_method': my_method,
                'start_date': start_date_data,
                'end_date': end_date_data,
                'state': state_data

            }
            return request.render("manthan_18_6_21.sale_order_front", vals)
        return request.render("manthan_18_6_21.sale_order_front")

    @http.route("/sale/all/data/<int:so_id>", type="http", auth="public", website=True)
    def SaleDatAall(self, so_id, **post):
        sale_details = request.env["sale.order"].browse([so_id])
        values = {}
        values.update({"sale_details": sale_details})
        return request.render("manthan_18_6_21.sale_order_detail_page", values)
