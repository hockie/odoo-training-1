{
    'name': 'Students Management',
    'summary': """Module to handle Students Management""",
    'description': """Module to handle:
        - Students
        - Activities
        - Lessons
        """,
    'license': 'OPL-1',
    'author': 'Hockie',
    'website': 'www.adeluuve.com',
    'category': 'Custom Modules/Tech Training',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/student_groups.xml',
        'security/ir.model.access.csv',
        'security/student_security.xml',
        'views/student_menuitems.xml',
        'views/student_views.xml',

    ],
    'demo': [
        'demo/student_demo.xml',
    ],
    'application': True,
}