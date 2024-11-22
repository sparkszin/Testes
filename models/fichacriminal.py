from datetime import date
from odoo import api, fields, models, _

class FichaCriminal(models.Model):
    _name = "fichacriminal"
    _description = "Modelo para Criar Fichas Criminais"
    
    sequence = fields.Char(
        string='Número da Ficha', 
        required=True, 
        copy=False, 
        readonly=True, 
        default=lambda self: _('Novo')
    )
    
    name = fields.Char(string='Nome', required=True)
    pic1 = fields.Binary(string='Foto 1' ,required=True)
    pic2 = fields.Binary(string='Foto 2')
    pic3 = fields.Binary(string='Foto 3')
    birthday = fields.Date(string='Data de Nascimento', required=True)
    age = fields.Integer(string='Idade', compute='_compute_age')
    gen = fields.Selection([
        ('mas','Masculino'),
        ('fem','Feminino'),
    ], string='Género', required=True)
    nasc = fields.Char(string='Nacionalidade', required=True)
    alt = fields.Integer(string='Altura (cm)', required=True)
    morada = fields.Char(string='Morada', required=True)
    cc = fields.Char(string='Nº Cartão Cidadão', required=True)
    nif = fields.Integer(string='NIF', required=True)
    seg = fields.Integer(string='Nº Segurança Social', required=True)
    ute = fields.Integer(string='Nº Utente de Saúde', required=True)
    fil = fields.Char(string='Filiação/Parentes', required=True)

    @api.depends('birthday')
    def _compute_age(self):
        """Compute the age based on the birth date."""
        for record in self:
            if record.birthday:
                today = date.today()
                born = record.birthday
                record.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            else:
                record.age = 0
                
    numero_ficha = fields.Integer(string='Números da Ficha', readonly=True)
                
    @api.model
    def create(self, vals):
        ultimo_registro = self.search([], order='numero_ficha desc', limit=1)
        novo_numero = ultimo_registro.numero_ficha + 1 if ultimo_registro else 1
        vals['numero_ficha'] = novo_numero
        return super(FichaCriminal, self).create(vals)