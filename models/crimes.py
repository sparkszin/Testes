from datetime import date
from odoo import api, fields, models

# Modelo dos Crimes 123
class Crimes(models.Model):
    _name = "crimes"
    _description = "Modelo para Criar Crimes"

    name = fields.Char(string='Nome do crime', required=True)