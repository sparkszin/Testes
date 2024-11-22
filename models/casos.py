import os
import psycopg2
from PIL import Image
from PIL.ExifTags import TAGS
from odoo import api, fields, models
import base64
from io import BytesIO

class RegistoCasos(models.Model):
    _name = "casos"
    _description = "Modelo para Registar Casos"

    name = fields.Char(string='Nome/Identificação', required=True)
    desc = fields.Text(string='Descritivo', required=True)
    data = fields.Date(string='Data de Registo', required=True)
    
    agente_id = fields.Many2one('agentes', string='Agente', required=True)
    casos_eq_ids = fields.Many2many('equipamentos', "eq_casos_id", string='Equipamentos Usados')
    
    
    def file_read(self):
        search_result = self.env['ir.attachment'].search([('res_id', '=', self.id)])  # Pesquisa os anexos
        
        for rec in search_result:
            print("###############################")
            print(rec.id)
            print(rec.name)
            print(rec.create_date)
            img_file = rec.datas
            
            img_data = BytesIO(base64.b64decode(img_file))
            image = Image.open(img_data)
            
            exif_data = image._getexif() 
            print (exif_data)
            
            #alterado
            