import frappe
from frappe import _
@frappe.whitelist(allow_guest=True)
def get_field_api_doctype(kwargs):
    doc = frappe.get_doc("DocType", 'DocType')
    return doc