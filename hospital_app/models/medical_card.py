from odoo import fields, models

class MedicalCard(models.Model):
    _name = "hospital.medical.card"
    _description = "Medical Card"
    
    patient_id = fields.Many2one("hospital.patient", string="Patient", required=True)
    doctor_id = fields.Many2one("hospital.doctor", string="Doctor", required=True)
    diagnosis_id = fields.Many2one("hospital.diagnosis", string="Diagnosis")
    visit_date = fields.Datetime(string="Visit Date", default=fields.Datetime.now)
    notes = fields.Text(string="Notes")
    
    