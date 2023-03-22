{
    'name': 'Clear Cart',
    'category': 'Website',
    'summary': 'Clear cart',
    'sequence': -1,
    'installable': True,
    'application': True,
    'depends': ['base', 'website_sale'],
    'data': ['views/clear_cart.xml'],
    'assets': {
        'web.assets_frontend': ['clear_cart/static/src/scss/clear_button.scss']
    }
}
