from datetime import date
from odoo import api, fields, models

class Cargos(models.Model):
    _name = "cargos"
    _description = "Modelo para Registar Cargos"

    name = fields.Char(string='Nome do Cargo', required=True)
    nivel = fields.Selection ([
        ('nivel1','Nível 1 - (Direção)'),
        ('nivel2','Nível 2 - (Carreira de Chefe / Carreira de Oficial)'),
        ('nivel3','Nível 3 - (Carreira de Agente)')
    ] , string='Nível', required=True)
    
    autor_ids = fields.One2many('autor' , 'cargos_id' , string='Agentes', readonly=True)
    