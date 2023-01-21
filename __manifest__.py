# -*- coding: utf-8 -*-
# Copyright 2020-23 Sohaib Khokhar
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

{
    'name': 'Patients',
    'version': '16.0',
    'summary': 'This module manage patients',
    'description': 'This module manage core patient',
    'category': 'Sales',
    'author': 'Sohaib',
    'maintainer': 'Sohaib Khokhar',
    'sequence': '10',
    'license': 'LGPL-3',
    'depends': [
        'base_setup',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/ibm_wiz.xml',
        'views/core_patient.xml',
        'views/care_plan.xml',
        'views/financial.xml',
        'views/notes.xml',
        'views/block_employee.xml',
        
    ],
    'installable': True,
    'auto_upgrade': True,
    'auto_install': False,
    'application': True,
}
