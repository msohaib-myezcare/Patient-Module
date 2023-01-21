# # -*- coding: utf-8 -*-

from odoo import api, fields, models, _



class CarePlan(models.Model):
    _name = 'financial'
    _description = 'Patient Financial'
    _rec_name = 'payor'

    payor = fields.Char(string='Payor', required=True)

    starting_date = fields.Date(string='Starting Date')

    end_date = fields.Date(string='End Date')

    precedence = fields.Char(string='Precedence')

    beneficiary_type = fields.Char(string='Beneficiary Type')

    beneficiary = fields.Char(string='Beneficiary')

    employee_school_name = fields.Char(string='Employee or School Name')

    insured_policy_group_feca_number = fields.Char(string='Insured Policy Group or FECA Number')

    member_id = fields.Integer(string='Member ID')

#This id Financial ID
    financial_id = fields.Many2one('core.patient', required=True)
#////////////////////

    checkbox_show_fields = fields.Boolean(string="Are you the primary member on insurance?")
#////////////////////

    f_name = fields.Char(string="First Name")

    m_name = fields.Char(string="Middle Name")

    l_name = fields.Char(string="Last Name")

    address = fields.Char(string="Address")

    city = fields.Many2one('res.country.state', string='City')

    state = fields.Many2one('res.country.state', string="State")

    zip_code = fields.Integer(string="Zip Code")
    
    phone = fields.Integer(string="Phone")

    date_of_birth = fields.Date("Date of birth")

    in_check_box_employee_school_name = fields.Char(string='Employee or School Name')

    in_check_box_insured_policy_group_feca_number = fields.Char(string='Insured Policy Group or FECA Number')



#This is Billing Setiing Fields

    facility_coder = fields.Char(string="Facility Coder")

    payor = fields.Char(string="Payor")

    rate = fields.Char(string="Rate")

    pay_rate = fields.Char(string="Pay Rate")

    revenue_code = fields.Char(string="Revenue Code")

    service_code = fields.Char(string="Service Code")

    unit_type = fields.Char(string="Unit Type")

    care_type = fields.Char(string="Care Type")

    taxonomy = fields.Char(string="Taxonomy")

    dxcode = fields.Char(string="DxCode")

    modifier = fields.Char(string="Modifier")

    authorization_code = fields.Char(string="Authorization Code")

    s_date = fields.Date(string='Start Date')

    e_date = fields.Date(string='End Date')

    attachment = fields.Binary(string='Attachment')



    states = fields.Selection([
        ('1', 'Info'),
        ('2', 'Care Plan'),
        ('3', 'Financial'),
        ('4', 'Schedule'),
        ('5', 'Finish'),
    ], string='Status', default='3')

    

    # def open_notes(self):
    #     for rec in self:
    #         notes_id = self.env['notes'].search([('notes_id', '=', rec.id)])
    #         if not notes_id:
    #             notes_id = self.env['notes'].create({
    #                 'notes_id': rec.id
    #             })
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': _('notes Form'),
    #         'res_model': 'notes',
    #         'views': [(self.env.ref("patient_configuration.notes_form").id, 'form')],
    #         'view_mode': 'form',
    #         'res_id': notes_id.id,
    #         'target': 'current',
    #         'nodestroy': True
    #     }




