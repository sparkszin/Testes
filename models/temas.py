from datetime import date
from odoo import api, fields, models

class Temas(models.Model):
    _name = "temas"
    _description = "Modelo para Criar Crimes"

    name = fields.Char(string='Nome do Crime', required=True)
    casos_ids = fields.Many2many('registodecasos' , string='Registos', required='True')