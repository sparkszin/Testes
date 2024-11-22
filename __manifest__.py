# -*- coding: utf-8 -*-
{
    'name' : 'Registo de Casos',
    'description': "",
    'version' : '1.0.0.0.0',
    'category': 'Productivity',
    'author' : 'Guilherme Duarte , Fábio Elvas',
    'license': 'AGPL-3',
    'contributors': [
        'Guilherme Duarte <guilherme33155@esfundao.pt>',
        'Fábio Elvas <fabio33567@esfundao.pt>' ,
    ],
    'depends' : [
        
    ],
    'data': [
        'views/casos.xml',
        'views/temas.xml',
        'views/autor.xml',
        'views/cargos.xml',
        'views/fichacriminal.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    
    'images':[
        'static/description/icon.png'
    ],
}