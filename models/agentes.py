from datetime import date
from odoo import api, fields, models

class Agentes(models.Model):
    _name = "agentes"
    _description = "Modelo para Criar Agentes"

    name = fields.Char(string='Nome do Agentes', required=True)
    birthday = fields.Date(string='Data de Nascimento', required=True)
    age = fields.Integer(string='Idade',compute='_compute_age')
    def _compute_age (self):
        for record in self:
            if record.birthday:
                today = date.today()
                born = record.birthday
                record.age = today.year - born.year - ((today.month,today.day) < (born.month,born.day))
            else:
                record.ag = 0
    morada = fields.Char(string='Morada', required=True)
    num = fields.Char(string='Número', required=True)
    cargo_id = fields.Many2one('cargos', string='Cargo', required=True)
    casos_ids = fields.One2many('casos', "agente_id", string='Processos' , readonly=True)