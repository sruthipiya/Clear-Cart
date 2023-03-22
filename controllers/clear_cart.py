from odoo import http
from odoo.http import request


class ClearCart(http.Controller):
    @http.route(['/action_clear'], type='http', auth="user", website=True, csrf=False)
    def _clear_shopping_cart(self):
        order = request.website.sale_get_order()
        order.order_line.unlink()
        # for line in order.order_line:
        #     line.unlink()
        return request.redirect("/shop/cart")

