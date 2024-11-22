from datetime import date
from odoo import api, fields, models

class RegistoCasos(models.Model):
    _name = "casos"
    _description = "Modelo para Registar Casos"

    name = fields.Char(string='Nome/Identificação', required=True)
    desc = fields.Text(string='Descritivo', required=True)
    data = fields.Date(string='Data de Registo', required=True)
    
    agente_id = fields.Many2one('agentes', string='Agente', required=True)
    casos_eq_ids = fields.Many2many('equipamentos', "eq_casos_id", string='Equipamentos Usados')
    