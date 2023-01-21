# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class Ibm(models.TransientModel):
    _name = 'm.core.bmi'

    # standard = fields.Boolean('Standard')
    # metric = fields.Boolean('Metric')
    # weight = fields.Float('Weight',required=True)
    # height = fields.Float('Height',required=True)
    # bmi = fields.Float('BMI')


    # def caluc(self):
    #     print('ibm')


    standard = fields.Boolean('Standard')
    metric = fields.Boolean('Metric')
    weight = fields.Float(string="Weight (kg)")
    height = fields.Float(string="Height (m)")
    bmi = fields.Float(string="BMI", compute='caluc')

    ibm_id = fields.Many2one('core.patient', required=True)

    def caluc(self):
        for record in self:
            if record.height and record.weight:
                record.bmi = record.weight / (record.height ** 2)

