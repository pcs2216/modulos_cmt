# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_cmt_partner(models.Model):
    _inherit = 'res.partner'

    x_cmt_validarListaPrecios = fields.Boolean(
        string='Validar lista de precios')
    x_cmt_validarCuestionario = fields.Boolean(
        string='Validar Cuestionario')
