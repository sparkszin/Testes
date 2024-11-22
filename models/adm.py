from datetime import date
from odoo import api, fields, models

# adm comentario como funciona?
class Adm(models.Model):
    _name = "adm"
    _description = "Modelo para Criar Administração"

    name = fields.Char(string='Administração', required=True)