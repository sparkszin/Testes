import os
import psycopg2
from PIL import Image
from PIL.ExifTags import TAGS
from odoo import api, fields, models
import base64
from io import BytesIO

class RegistoCasos(models.Model):
    _name = "registodecasos"
    _description = "Modelo para Registar Casos"

    ficha_id = fields.Many2one('fichacriminal', string='Nome do suspeito', required=True)
    desc = fields.Text(string='Descritivo', required=True)
    data = fields.Date(string='Data de Registo', required=True)
    autor_id = fields.Many2one('autor', string='Agente Responsável')
    temas_ids = fields.Many2many('temas', string='Crime(s) Cometidos', required=True)
    provas = fields.Binary(string="Documento Anexado")

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
            
             

            
            
            
    



