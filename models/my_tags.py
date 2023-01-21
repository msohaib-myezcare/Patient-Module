# # -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ServiceTags(models.Model):
    _name = 'service.tags'
    _description = 'Service Tags'



    name = fields.Char(string='name')











class ContactTags(models.Model):
    _name = 'contact.tags'
    _description = 'Contact Tags'


    name = fields.Char(string="name")




class CareTags(models.Model):
    _name = 'care.tags'
    _description = 'care Tags'


    name = fields.Char(string="name")