from odoo import http

class ModuleName(http.Controller):
    @http.route('/compare', auth='public', website=True, sitemap=False)
    def module_feature(self,**kw):
        motorcycles = http.request.env['product.template'].search([('detailed_type','=','motorcycle')])
        values = {
            'products': motorcycles.with_context(display_default_code=False)
        }
        return http.request.render('motorcycle_registry.motorcycle_compare', values)


