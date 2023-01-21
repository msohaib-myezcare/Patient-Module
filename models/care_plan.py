# # -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class CarePlan(models.Model):
    _name = 'care.plan'
    _description = 'Patients Care Plan'
    _rec_name = 'patients_id'

    task = fields.Selection([
        ('task', 'Task'),
        ('conclusion', 'Conclusion')
    ], string='Task', default='task', required=True)
    
    care_type = fields.Selection([
        ('care_type', 'Care Type'),
        ('personal_care', 'Personal Care'),
        ('respite_care', 'Respite Care')
        ], string='Care Type', default='care_type')

    goal = fields.Char(string="Goal")

    patients_id = fields.Many2one('core.patient', required=True)

    states = fields.Selection([
        ('1', 'Info'),
        ('2', 'Care Plan'),
        ('3', 'Financial'),
        ('4', 'Schedule'),
        ('5', 'Finish'),
    ], string='Status', default='2')

    #This is Patient Schedule Fields..

    check_show_fields = fields.Boolean(string="Show Fields")

    referral = fields.Many2one('res.partner', string="Referral")

    select_patient_filter = fields.Selection([
        ('1', 'Active'),
        ('2', 'Expired'),
        ('3', 'Delete'),
    ], string='Patient Filter', default='1')

    start_date = fields.Date(string="Start Date")

    end_date = fields.Date(string="End Date")


    # def open_financial(self):
    #     for rec in self:
    #         financial_id = self.env['financial'].search([('financial_id', '=', rec.id)])
    #         if not financial_id:
    #             financial_id = self.env['financial'].create({
    #                 'financial_id': rec.id
    #             })
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': _('Financial Form'),
    #         'res_model': 'financial',
    #         'views': [(self.env.ref("patient_configuration.financial_form").id, 'form')],
    #         'view_mode': 'form',
    #         'res_id': financial_id.id,
    #         'target': 'current',
    #         'nodestroy': True
    #     }
















































































































