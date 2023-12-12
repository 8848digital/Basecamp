# import frappe

# @frappe.whitelist(allow_guest=True)
# def get_list_view(kwargs):
#     # Get metadata of the 'Custom Form' DocType
#     custom_form_meta = frappe.get_meta("Custom Form")
    
#     # Extract fields information
#     fields_info = [field.fieldname for field in custom_form_meta.fields if field.in_list_view == 1 ]
    
#     # Convert list of strings to list of dictionaries
#     fields_as_objects = [{"label": field} for field in fields_info]
    
#     fields_as_objects.append({"label": "name"})  # Append "name" separately as an object
    
#     return fields_as_objects


# import frappe

# @frappe.whitelist(allow_guest=True)
# def get_list_view_data(kwargs):
#     # Get metadata of the 'Custom Form' DocType
#     docname = kwargs.get("doc_name")
#     custom_form_meta = frappe.get_meta(docname)
    
#     # Extract fields information
#     fields_info = [field.fieldname for field in custom_form_meta.fields if field.in_list_view == 1 ]
#     fields_info.append("name")
    

#     custom_form_list = frappe.get_list(docname,fields_info)

    
#     return custom_form_list
