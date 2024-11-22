from datetime import date
from odoo import api, fields, models

class Equipamentos(models.Model):
    _name = "equipamentos"
    _description = "Modelo para Criar Equipamentos"

    name = fields.Char(string='Equipamentos', required=True)
    cargos_id = fields.Many2one('cargos', string='Cargos')
    eq_casos_id = fields.Many2many('casos', string='Equipamentos 2')
    