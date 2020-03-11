#
#
# en data almacenamos los archivos de registro como los de seguridad siempre con rutas relativas
{
    'name': "HelpDesk Curso",
    'summary': "Module to Support Teams",
    'version': '13.0.1.0.0',
    'category': 'Customer Relationship Management',
    'website': "",
    'author': "Belen Lopez",
    'license': "AGPL-3",
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_ticket_views.xml", ],
    'application': True,
    'installable': True,
}
