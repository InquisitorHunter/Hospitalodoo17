from odoo import fields, models

class Diagnosis(models.Model):
    _name = "hospital.diagnosis"
    _description = "Diagnosis"
    
    name = fields.Char(String = "Diagnosis Name", required=True)
    description = fields.Text(string="Description")
    medicalcard_id = fields.One2many("hospital.medical.card", "diagnosis_id", String = "Medical Card")