from odoo import fields, models

class Doctor(models.Model):
    _name = "hospital.doctor"
    _description = "Doctor"
    
    name = fields.Char(String = "Full Name", required=True)
    phone = fields.Char(String = "Phone", required=True)
    email = fields.Char(String = "Email", required=True)
    specialty = fields.Char(string="Specialty")
    patient_id = fields.Many2one("hospital.medical.card", string="Patient")