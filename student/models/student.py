from odoo import fields, models

class Student(models.Model):
    _name = "student.student"
    _description = "Student Module"
    
    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    
    description = fields.Text()