# import frappe
# from frappe import _

# @frappe.whitelist(allow_guest=True)
# def get_form(kwargs):
#     try:
#         data = frappe.db.sql("""
#             SELECT *
#             FROM
#                 `tabForm` AS ch
                                     
#             ORDER BY
#                     modified desc
#         """, as_dict=True)
#         return build_response("success", data=data)
#     except Exception as e:
#         frappe.log_error(title=_("API Error"), message=str(e))
#         return build_response("error", message=_("An error occurred while fetching data."))

# def build_response(status, data=None, message=None):
#     response = {
#         "status": status
#     }

#     if data is not None:
#         response["data"] = data

#     if message is not None:
#         response["message"] = message

#     return response
