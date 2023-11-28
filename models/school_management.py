from odoo import models,fields,api
class school_management(models.Model):
    _name = "school.student"
    _description = "School Management"

    name = fields.Many2one('res.partner',string="Student")
    class_id = fields.Integer(string="Class")
    divison = fields.Char(string="Divison")

