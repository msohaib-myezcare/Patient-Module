# # -*- coding: utf-8 -*-

from odoo import api, fields, models, _



class Notes(models.Model):
    _name = 'notes'
    _description = 'Patient Notes'
    _rec_name = 'notes_id'


    def open_block_employee(self):
        for rec in self:
            block_id = self.env['block.employee'].search([('block_id', '=', rec.id)])
            if not block_id:
                block_id = self.env['block.employee'].create({
                    'block_id': rec.id
                })
        return {
            'type': 'ir.actions.act_window',
            'name': _('Block Employee Form'),
            'res_model': 'block.employee',
            'views': [(self.env.ref("patient_configuration.block_employee_form").id, 'form')],
            'view_mode': 'form',
            'res_id': block_id.id,
            'target': 'current',
            'nodestroy': True
        }


    states = fields.Selection([
        ('1', 'Info'),
        ('2', 'Care Plan'),
        ('3', 'Financial'),
        ('4', 'Notes'),
        ('5', 'Block Employee'),
        ('6', 'Schedule'),
        ('7', 'Finish'),
    ], string='Status', default='4')

#This id Note ID
    notes_id = fields.Many2one('core.patient', required=True)
#////////////////////
    module_lines = fields.One2many('notemodule.lines','module_id', string="Modules")








class NoteModuleLines(models.Model):
    _name = 'notemodule.lines'
    _description = 'Notebook Tree View'

    module_id = fields.Many2one("notes", string="Module")
    
    note = fields.Char(string="Note", required=True)

    added_by = fields.Char(string="Added By")

    category = fields.Char(string="Category")

    added_date = fields.Date(string="Added Date")

    is_private = fields.Boolean(string="Is Private")


    