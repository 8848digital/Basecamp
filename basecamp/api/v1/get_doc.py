# import frappe
# from frappe import _

# @frappe.whitelist(allow_guest=True)
# def get_doctype(kwargs):
#     try:
#         docname = kwargs.get("doc_name")
#         if not docname:
#             return _("Document name not provided.")

#         doc = frappe.get_doc("DocType", docname)
#         return doc
#     except frappe.DoesNotExistError:
#         return _("DocType '{}' not found.").format(docname)
#     except Exception as e:
#         return _("An error occurred: {}").format(str(e))
