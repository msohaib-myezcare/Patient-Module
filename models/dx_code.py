from odoo import models, fields, api
import requests


class CoreIcd10cmCode(models.Model):
    _name = 'core.icd10cm.code'
    _description = 'M Core HCPCS Code'
    _rec_name = "code"

    code = fields.Char(string="Service Code", help="Unique code of the service.")
    name = fields.Char(string="Service Name", help="Name of the service.")

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        res = super(CoreIcd10cmCode, self).name_search(name=name, args=args, operator=operator, limit=limit)
        if self._context.get('from_icd10cm_code') and not res:
            icd10cm_data = self.get_icd10cm_data(kw_search=name)
            new_icd10cm_data = self.store_icd10cm_data(icd10cm_data=icd10cm_data)
            res = new_icd10cm_data
        return res

    def store_icd10cm_data(self, icd10cm_data):
        """
        Stores the icd10cm data in local database, skips storing the data if code already exists in local database
        :param icd10cm_data: list - list of dict
        :return: list - list of tuple
        """
        icd10cm_list_tuple = []
        existing_icd10cm_codes = list(map(lambda l: l.get('code'), self.search_read([], ['code'])))
        icd10cm_data = list(filter(lambda c: c.get('code') not in existing_icd10cm_codes, icd10cm_data))
        for data in icd10cm_data:
            icd10cm_id = self.create(
                {'code': data.get('code'), 'name': data.get('name')})
            icd10cm_list_tuple.append((icd10cm_id.id, "%s" % icd10cm_id.code))
        return icd10cm_list_tuple

    def get_icd10cm_data(self, kw_search):
        """
        Calls HCPCS API to get the code and other data which best matches the search string
        :param kw_search: str - keyword to search for related data
        :return:
        """
        parameters = {
            "terms": kw_search,
            "df": "code, name"
        }
        response = requests.get(url="https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search", params=parameters)
        json_data = response.json()
        icd10cm_data = self.prepare_icd10cm_data_dict(icd10cm_data_list=json_data[3])
        return icd10cm_data


    def prepare_icd10cm_data_dict(self, icd10cm_data_list):
        """
        Prepares the list of dictionary for icd10cm data
        :param icd10cm_data_list: list
        :return: list - list of dict
        """
        icd10cm_data = []
        keys = ['code', 'name']
        for data in icd10cm_data_list:
            icd10cm_dict = {}
            for i, d in enumerate(data):
                icd10cm_dict.update({keys[i]: d})
            icd10cm_data.append(icd10cm_dict)
        return icd10cm_data
