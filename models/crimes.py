from datetime import date
from odoo import api, fields, models

class Crimes(models.Model):
    _name = "crimes"
    _description = "Modelo para Criar Crimes"

    name = fields.Char(string='Nome do crime', required=True)