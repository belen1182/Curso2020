#
#
# en data almacenamos los archivos de registro como los de seguridad siempre co
# n rutas relativas
{
    'name': "HelpDesk Curso",
    'summary': "Module to Support Teams",
    'version': '13.0.1.0.0',
    'category': 'Customer Relationship Management',
    'website': "",
    'author': "Belen Lopez",
    'license': "AGPL-3",
    'data': [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "wizard/helpdesk_set_responsable_views.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_team_views.xml",
        "views/helpdesk_stage_views.xml",
        "views/res_users_views.xml",
        "views/menu.xml",

        ],
    'depends':[
        "base",
        "mail",
        ],
    'application': True,
    'installable': True,
}
