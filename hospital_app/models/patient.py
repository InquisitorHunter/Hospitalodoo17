from odoo import fields, models

class Patient(models.Model):
    _name = "hospital.patient"
    _description = "Patient"
    
    name = fields.Char(string="Full Name", required=True)
    gender = fields.Selection(
        selection=[
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="Gender",
        required=True)
    date_of_birth = fields.Date(string="Date Of Birth")
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email", required=True)
    medicalcard_ids = fields.One2many(
        "hospital.medical.card",
        "patient_id",
        string="Medical Cards"
        )