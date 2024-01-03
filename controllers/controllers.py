# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class SkillMan(http.Controller):
    @http.route('/', type='http', auth='public', website=True)
    def index(self, **kw):
        return request.render('skillman_web.home')

    @http.route('/gender', type='http', auth='public', website=True)
    def index(self, **kw):
        return request.render('skillman_web.gender')

    @http.route('/advisory', type='http', auth='public', website=True)
    def index(self, **kw):
        return request.render('skillman_web.advisory')

    @http.route('/webinars', type='http', auth='public', website=True)
    def index(self, **kw):
        return request.render('skillman_web.webinars')

    @http.route('/plcone', type='http', auth='public', website=True)
    def index(self, **kw):
        return request.render('skillman_web.plc_one')

#     @http.route('/skillman_web/skillman_web/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('skillman_web.listing', {
#             'root': '/skillman_web/skillman_web',
#             'objects': http.request.env['skillman_web.skillman_web'].search([]),
#         })

#     @http.route('/skillman_web/skillman_web/objects/<model("skillman_web.skillman_web"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('skillman_web.object', {
#             'object': obj
#         })
