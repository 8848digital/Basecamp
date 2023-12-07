# import frappe
# from frappe import _

# @frappe.whitelist(allow_guest=True)
# def create_doctype(kwargs):
#     try:
#         docname = kwargs.get("doc_name")
#         mod = kwargs.get("module")
#         submittable = kwargs.get("is_submittable")
#         issingle = kwargs.get("issingle")
#         istable = kwargs.get("istable")
#         autoname = kwargs.get("autoname")
#         naming_rule = kwargs.get("naming_rule")


#         fields = kwargs.get('fields', [])
#         permissions = kwargs.get('permissions', [])
        
#         try:
#             existing_doctype = frappe.get_doc("DocType", docname)
#             existing_doctype.naming_rule = naming_rule
#             existing_doctype.autoname = autoname

            
#             # Doctype exists, update fields
#             for row in fields:
#                 existing_field = next((f for f in existing_doctype.fields if f.idx == row.get('idx')), None)
#                 if existing_field:
#                     # Update existing field
#                     fieldtype = row.get('fieldtype', '')
#                     options = row.get('options', '') if fieldtype == 'Link' or fieldtype == 'Select' else ''
#                     existing_field.update({
#                         "idx": row.get('idx', ''),
#                         "label": row.get('label', ''),
#                         "fieldtype": fieldtype,
#                         "options": options
#                     })
#                 else:
#                     # Add new field
#                     field_dict = {
#                         "idx": row.get('idx', ''),
#                         "label": row.get('label', ''),
#                         "fieldtype": row.get('fieldtype', ''),
#                     }
#                     fieldtype = row.get('fieldtype', '')
#                     options = row.get('options', '') if fieldtype == 'Link' or fieldtype == 'Select' else ''
#                     if options:
#                         field_dict["options"] = options
#                     existing_doctype.append("fields", field_dict)
            
#             existing_doctype.save(ignore_permissions=True)
#             return {"msg": "success", "doc": existing_doctype.as_dict()}
        
#         except frappe.DoesNotExistError:
#             # Doctype does not exist, create a new one
#             doc = frappe.new_doc("DocType")
#             doc.name = docname
#             doc.module = mod
#             doc.is_submittable = submittable
#             doc.issingle = issingle
#             doc.istable = istable
#             doc.naming_rule = naming_rule
#             doc.autoname = autoname
            
#             for row in fields:
#                 field_dict = {
#                     "idx": row.get('idx', ''),
#                     "label": row.get('label', ''),
#                     "fieldtype": row.get('fieldtype', ''),
#                 }
#                 fieldtype = row.get('fieldtype', '')
#                 options = row.get('options', '') if fieldtype == 'Link' or fieldtype == 'Select'  or  fieldtype == 'Attach Image' else ''
#                 if options:
#                     field_dict["options"] = options
#                 doc.append("fields", field_dict)
            
#             for row in permissions:
#                 doc.append("permissions", {
#                     "role": row.get('role', ''),
#                     "read": row.get('read', ''),
#                     "write": row.get('write', ''),
#                     "create": row.get('create', ''),
#                     "delete": row.get('delete', ''),
#                     "submit": row.get('submit', ''),
#                     "cancel": row.get('cancel', '')
#                 })
#             doc.save(ignore_permissions=True)
#             return {"msg": "success", "doc": doc.as_dict()}
    
#     except frappe.ValidationError as e:
#         frappe.logger().error(f"Validation error: {e}")
#         return {"msg": "error", "error": str(e)}
    
#     except Exception as e:
#         frappe.logger().error(f"Unexpected error: {e}")
#         return {"msg": "error", "error": str(e)}
