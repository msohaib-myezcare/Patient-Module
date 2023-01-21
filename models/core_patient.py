# # -*- coding: utf-8 -*-
import secrets

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from xml.dom import ValidationErr
from odoo import models, fields,_ 

class CorePatient(models.Model):
    _name = 'core.patient'
    _inherit = {'mail.thread', 'mail.activity.mixin'}
    _description = 'Patients'
    _rec_name = 'first_name'



#This is a form view Patient
    first_name = fields.Char(string='First Name', required=True)

    age = fields.Char(string="Age")


    last_name = fields.Char(string='Last Name')
    
    middle_name = fields.Char(string='Middle Name')
    
    date_of_birth = fields.Date("Date of birth")
    
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')],
        string="Gender", tracking=True)
    
    lang = fields.Selection(selection=[
    ('1', 'English'),
    ('2', 'Other'),
    ('3', 'Spanish'),
    ('4', 'Chinese')],string="Lang. Preference")
    
    account = fields.Integer(string='Account#')
    
    location = fields.Char(string='Location', size=64, geo_point=True)
    
    status = fields.Selection(selection=[
    ('1', 'Active'),
    ('2', 'Pro Bono'),
    ('3', 'Inactive'),
    ('4', 'Discharged'),
    ('5', 'New Referral'),
    ('6', 'Incomplete Referral'),
    ('7', 'Inactive Referral '),
    ('8', 'Dormant Referral'),
    ('9', 'Referral Accepted'),
    ('10', 'Referral Initial Review'),
    ('11', 'On Hold'),
    ('12', 'Denied'),
    ('13', 'Transfer'),
    ('14', 'Referral')],string="Status")

    groups = fields.Char(string='Groups')
    
    assignee = fields.Many2one('hr.employee', string='Assignee')

    care_tags = fields.Many2many('care.tags', string='Care Type', widget="many2many_tags")

    ssn = fields.Integer(string="SSN", size=11)

    service_tags = fields.Many2many('service.tags', string='Service Type')

#//////////////////////////////////////////
    def action_confirm(self):
        # code to be executed
        return True

#This Is a COntact Details Notebook Fields

    # contact_type = fields.Char(string="Contact Type")

    # cemail = fields.Char(string="Email")
    
    # is_emergency_contact = fields.Char(string="Is Emergency Contact")
    
    # state = fields.Many2one('res.country.state', string="State")

    # f_name = fields.Char(string="First Name")

    # l_name = fields.Char(string="Last Name")

    # primary_number = fields.Integer(string="Primary Number")

    # address = fields.Char(string="Address")

    # zip_code = fields.Integer(string="Zip Code")

    # city = fields.Many2one('res.country.state', string='City')

    # alternate_number = fields.Integer(string="Alternate Number")

    # language_preference = fields.Char(string="Language Preference")

    # apartment_no = fields.Integer(string="Apartment No")

# This Is a History Notebook Fields


    # service_type = fields.Selection(string="Service Type",selection=[
    # ('1', 'Agency-Directed Service'),
    # ('2', 'Consumer-Directed Service'),
    # ('3', 'Consumer Directed'),
    # ('4', 'Agency Directed'),
    # ('5', 'Consumer-Directed Service')])


    blood_group = fields.Char(string="Blood Group")

    ethnicity = fields.Char(string="Ethnicity")

    race = fields.Char(string="Race")

#//////////////////////////////////////////

#This Is a DXCode Notebook Fields

    # dxcode_type = fields.Selection(string="DxCode Type",selection=[
    # ('dx10', 'ICD-10-CM'),
    # ('dx9', 'ICD-9-CM')])

    # dxcode = fields.Char(string="DxCode")

    # precedence = fields.Char(string="Precedence")

    # description = fields.Text(string="Description ")

    # dxcode_without_dot = fields.Char(string="DxCode Without Dot")


#This Is a Physician Notebook Fields

    module_line_ids_physician = fields.One2many('module.lines','module_id')

#This Is a Allergy Notebook Fields

    allergy = fields.Char(string="Allergy")

    causative_agent = fields.Many2one('res.partner', string='Causative Agent')
    
    observed = fields.Boolean(string="Observed")

    historical = fields.Boolean(string="Historical")

    reported_by = fields.Many2one(comodel_name='res.users', string='Reported By')

    reaction = fields.Char(string="Reaction")

    comments = fields.Char(string="Comments")

    module_line_ids_allergy = fields.One2many('module.lines','module_id')

    module_line_ids_dxcode = fields.One2many('module.lines','module_id')
    
    module_line_ids_contacts = fields.One2many('kanban.lines','vat')

#This Is a Medication Notebook Fields
    
    search_medication = fields.Char(string="Search Medication")

    route = fields.Char(string="Route")

    physician = fields.Char(string="Physician")

    patient_instructions = fields.Char(string="Patient Instructions")

    strength = fields.Integer(string="Strength")

    quantity = fields.Integer(string="Quantity")

    health_diagnostics = fields.Char(string="Health Diagnostics")

    pharmacist_instructions = fields.Char(string="Pharmacist instructions")

    units = fields.Float(string='Units', digits=(10,2), default=1.0)

    start_date = fields.Date(string="Start Date")
    
    end_date = fields.Date(string="End Date")

    frequency = fields.Char(string="Frequency")

    # active = fields.Boolean(string="Active")

    # in_active = fields.Boolean(string="Inactive")


#This is Equipment Notebook Fileds


    preference = fields.Char(string="Preference")

    required_skills = fields.Selection(string="Required Skills",selection=[
    ('1', 'First Aid'),
    ('2', 'CPR Certification'),
    ('3', 'Oxygen Dependent'),
    ('4', 'Do Not Rescusitate'),
    ('5', 'ADVANCE DIRECTIVE'),
    ('6', 'Power of Attorney'),
    ('7', 'Nurse Tester')])

#This is settings Notebook Fileds


    image = fields.Binary(string="Image")
    

    name = fields.Char(string="Name")
    login = fields.Char(string="Login")
    email = fields.Char(string="Email")
    password = fields.Char(string="Password")



    def create_user(self):
        user = self.env['res.users'].create({
            'name': self.name,
            'login': self.login,
            'email': self.email,
            'password': self.password,
        })


    states = fields.Selection([
        ('1', 'Info'),
        ('2', 'Care Plan'),
        ('3', 'Financial'),
        ('4', 'Schedule'),
        ('5', 'Finish'),
    ], string='Status', default='1')


    def open_care_plan(self):
        for rec in self:
            care_plan_id = self.env['care.plan'].search([('patients_id', '=', rec.id)])
            if not care_plan_id:
                care_plan_id = self.env['care.plan'].create({
                    'patients_id': rec.id
                })
        return {
            'type': 'ir.actions.act_window',
            'name': _('Care Plan Form'),
            'res_model': 'care.plan',
            'views': [(self.env.ref("patient_configuration.core_plan_form").id, 'form')],
            'view_mode': 'form',
            'res_id': care_plan_id.id,
            'target': 'current',
            'nodestroy': True
        }



    # display_name = fields.Char(string='Name', required=True)

    # email = fields.Char('Email', required=True)
    
    # mobile = fields.Char('Mobile', required=True)


    def open_financial(self):
        for rec in self:
            financial_id = self.env['financial'].search([('financial_id', '=', rec.id)])
            if not financial_id:
                financial_id = self.env['financial'].create({
                    'financial_id': rec.id
                })
        return {
            'type': 'ir.actions.act_window',
            'name': _('Financial Form'),
            'res_model': 'financial',
            'views': [(self.env.ref("patient_configuration.financial_form").id, 'form')],
            'view_mode': 'form',
            'res_id': financial_id.id,
            'target': 'current',
            'nodestroy': True
        }


    def open_notes(self):
        for rec in self:
            notes_id = self.env['notes'].search([('notes_id', '=', rec.id)])
            if not notes_id:
                notes_id = self.env['notes'].create({
                    'notes_id': rec.id
                })
        return {
            'type': 'ir.actions.act_window',
            'name': _('notes Form'),
            'res_model': 'notes',
            'views': [(self.env.ref("patient_configuration.notes_form").id, 'form')],
            'view_mode': 'form',
            'res_id': notes_id.id,
            'target': 'current',
            'nodestroy': True
        }


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




































class ModuleLines(models.Model):
    _name = 'module.lines'
    _description = 'Notebook Tree View'

    module_id = fields.Many2one("core.patient")

    physician = fields.Char(string="Physician")

    address = fields.Char(string="Address")    

    phone = fields.Integer(string="Phone")    

    Specialist = fields.Float(string="Specialist")



#This field is allergy

    causative_agents = fields.Char(string="Causative Agent")

    status = fields.Char(string="Status")

    date = fields.Date(string="Date")

    reaction = fields.Char(string="Reaction")

    reported_by = fields.Many2one(comodel_name='res.users', string='Reported By')

    
    dxcode = fields.Char(string="DxCode")

    precedence = fields.Char(string="Precedence")

    description = fields.Text(string="Description ")

    dxcode_without_dot = fields.Char(string="DxCode Without Dot")


#/////////////////////////
#/////////////////////////
#/////////////////////////
#/////////////////////////
#/////////////////////////
 #This Function Call DxCode Relationship to Models in dxcode.py file

    icd10cm_code_id = fields.Many2one(comodel_name="core.icd10cm.code", string="DxCode",
                                    help="Unique code of the service.")
    name = fields.Char(string="Name", help="Name of the service.")
    # modifier_id = fields.Many2one(comodel_name="m.core.service.modifier", string="Modifier")
    # is_billable = fields.Selection(selection=[('Yes', 'Yes'), ('No', 'No')], string="Is Billable?")

    @api.onchange('icd10cm_code_id')
    def onchange_icd10cm_code(self):
        """
        Set icd10cm name on change of icd10cm code
        """
        if self.icd10cm_code_id:
            self.name = self.icd10cm_code_id.name

#////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////



class KanbanLines(models.Model):
    _name = 'kanban.lines'
    _description = 'Notebook Kanban View'



    


    

    name = fields.Many2one('res.partner',string='Name')

    street = fields.Char(string='Street')

    street2 = fields.Char(string='Street2')

    city = fields.Char(string='City')

    contact_tags = fields.Many2many('contact.tags', string='Service Type', widget="many2many_tags")

    state_id = fields.Many2one('res.country.state', string="State")

    zip = fields.Char(string='Zip')

    country_id = fields.Many2one('res.country', string="Country")

    phone = fields.Char(string='Phone')

    mobile = fields.Char(string='Mobile')

    email = fields.Char(string='Email')

    image_1920 = fields.Binary(string="Image", widget="image")
    
    vat = fields.Many2one("core.patient", string="Tax", readonly=True)
    
    

    @api.onchange('name')
    def onchange_name(self):
        if not self.name:
            return
        self.street = self.name.street
        self.street2 = self.name.street2
        self.city = self.name.city
        self.state_id = self.name.state_id
        self.zip = self.name.zip
        self.country_id = self.name.country_id
        self.phone = self.name.phone
        self.mobile = self.name.mobile
        self.email = self.name.email
        self.image_1920 = self.name.image_1920
        self.vat = self.name.vat




    

























