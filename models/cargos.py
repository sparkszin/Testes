from datetime import date
from odoo import api, fields, models

class Cargos(models.Model):
    _name = "cargos"
    _description = "Modelo para Criar Cargos"

    name = fields.Char(string='Cargo', required=True)
    agentes_ids = fields.One2many('agentes', "cargo_id", string='Agentes')
    equipamentos_ids = fields.One2many('equipamentos', "cargos_id", string='Equipamentos')