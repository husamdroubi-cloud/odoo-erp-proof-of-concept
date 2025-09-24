{
    'name': 'Master Parts List Manager',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Manage master list of parts and components',
    'description': """
        Proof of Concept Odoo module to manage a master list of parts.
        Features:
        - Central parts catalog
        - Categories & attributes
        - Search & reporting
    """,
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/parts_views.xml',
    ],
    'installable': True,
    'application': True,
}
