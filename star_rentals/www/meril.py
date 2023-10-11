import frappe

def get_context(context):
    current_user = frappe.get_doc("User", frappe.session.user)
    context.current_user = current_user
