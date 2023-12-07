import frappe
from basecamp.utils import success_response, error_response
import basecamp.api.v1.access_token as access_token
import basecamp.api.v1.create_doc as create_doc
import basecamp.api.v1.get_doc as get_doc
import basecamp.api.v1.form_api as form_api
import basecamp.api.v1.get_field_doctype as get_field_doctype
import basecamp.api.v1.get_doc_child_table as get_doc_child_table







class V1():
    def __init__(self):
        self.methods = {
            'access_token':['get_access_token'],
            'create_doc':['create_doctype'],
            'get_doc':['get_doctype'],
            'form_api':['get_form'],
            'get_field_doctype':['get_field_api_doctype'],
            'get_doc_child_table':['get_doctype_child_table']

            
            
        }
    def class_map(self, kwargs):
        entity = kwargs.get('entity')
        method = kwargs.get('method')
        if self.methods.get(entity):
            if method in self.methods.get(entity):
                function = f"{kwargs.get('entity')}.{kwargs.get('method')}({kwargs})"
                return eval(function)
            else:
                return error_response("Method Not Found!")
        else:
            return error_response("Entity Not Found!")
