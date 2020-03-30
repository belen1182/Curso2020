#
#
# en data almacenamos los archivos de registro como los de seguridad siempre co
# n rutas relativas
{
    'name': "Displacement Employee",
    'summary': "Module for the control of employee movements",
    'version': "13.0.1.0.0",
    'category': "Customer Relationship Management",
    'website': "",
    'author': "Belen Lopez",
    'license': "AGPL-3",
    'data': [
        "security/displacement_security.xml",
        "security/ir.model.access.csv",
        "views/displacement_travel.xml",
        "views/displacement_menu.xml",
    ],
    'application': True,
    'installable': True,
}
