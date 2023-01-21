# # -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class CarePlan(models.Model):
    _name = 'block.employee'
    _description = 'Patients Block Employee'
    _rec_name = 'block_id'

    
    

    states = fields.Selection([
        ('1', 'Info'),
        ('2', 'Care Plan'),
        ('3', 'Financial'),
        ('4', 'Notes'),
        ('5', 'Block Employee'),
        ('6', 'Schedule'),
        ('7', 'Finish'),
    ], string='Status', default='5')

#This id Note ID
    block_id = fields.Many2one('core.patient', required=True)
#////////////////////
    module_lines = fields.One2many('blockmodule.lines','module_id', string="Modules")

class BlockModuleLines(models.Model):
    _name = 'blockmodule.lines'
    _description = 'Notebook Tree View'

    module_id = fields.Many2one("block.employee", string="Module")

    employee = fields.Char(string="Employee", required=True)

    blocking_reason = fields.Char(string="Blocking Reason")

    blocking_requested_by = fields.Char(string="Blocking Requested by")

    blocked_date = fields.Date(string="Blocked Date")



















































