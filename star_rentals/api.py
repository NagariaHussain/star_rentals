import frappe

@frappe.whitelist()
def get_emoji():
    return frappe.form_dict.top_secret 

def send_otp():
    pass