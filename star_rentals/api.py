import frappe

@frappe.whitelist()
def get_emoji():
    return "something" 

def send_otp():
    pass

def get_permission_query():
    current_user = frappe.session.user
    user_doc = frappe.get_doc("User", current_user)

    query = "<all_query>"
    if reports_to_manager(user_doc):
        return query + 'AND ...'

    return

def reports_to_manager(user_doc):
    return


def takes_10_seconds():
   import time
   time.sleep(10) 
