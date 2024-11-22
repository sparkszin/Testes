from datetime import date
from odoo import api, fields, models

class Autor(models.Model):
    _name = "autor"
    _description = "Modelo para Criar Agentes"

    name = fields.Char(string='Nome do Agente', required=True)
    birthday = fields.Date(string='Data de Nascimento', required=True)
    age = fields.Integer(string='Idade',compute='_compute_age')
    def _compute_age (self):
        for record in self:
            if record.birthday:
                today = date.today()
                born = record.birthday
                record.age = today.year - born.year - ((today.month,today.day) < (born.month,born.day))
            else:
                record.age = 0
    morada = fields.Char(string='Morada', required=True)
    num = fields.Char(string='Número', required=True)
    
    cargos_id = fields.Many2one('cargos', string="Cargo", required=True)
    casos_ids = fields.One2many('registodecasos' , 'autor_id' , string='Processos', readonly=True)
    
    
    #@api.onchange('cargo_id')
    #def _update_user_group(self):
    #    if self.cargo_id:
    #        user = self.env['res.users'].browse(self.env.uid)
    #        # Remove todos os grupos de cargo para adicionar o correto
    #        user.groups_id -= self.env.ref('gestao.group_junior')
    #        user.groups_id -= self.env.ref('gestao.group_pleno')
    #        user.groups_id -= self.env.ref('gestao.group_senior')
    #        # Adiciona o grupo correto baseado no cargo
    #        if self.cargo_id.nivel == 'junior':
    #            user.groups_id |= self.env.ref('gestao.group_junior')
    #        elif self.cargo_id.nivel == 'pleno':
    #            user.groups_id |= self.env.ref('gestao.group_pleno')
    #        elif self.cargo_id.nivel == 'senior':
    #            user.groups_id |= self.env.ref('gestao.group_senior')
    