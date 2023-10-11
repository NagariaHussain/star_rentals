app_name = "star_rentals"
app_title = "Star Rentals"
app_publisher = "Hussain"
app_description = "For managing vehicle and drivers for Irfan Cabs Co."
app_email = "hussain@frappe.io"
app_license = "mit"
# required_apps = []


fixtures = [
    "Vehicle Type"
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/star_rentals/css/star_rentals.css"
# app_include_js = "/assets/star_rentals/js/star_rentals.js"

# include js, css files in header of web template
# web_include_css = "/assets/star_rentals/css/star_rentals.css"
# web_include_js = "/assets/star_rentals/js/star_rentals.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "star_rentals/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "star_rentals/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "star_rentals.utils.jinja_methods",
#	"filters": "star_rentals.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "star_rentals.install.before_install"
# after_install = "star_rentals.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "star_rentals.uninstall.before_uninstall"
# after_uninstall = "star_rentals.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "star_rentals.utils.before_app_install"
# after_app_install = "star_rentals.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "star_rentals.utils.before_app_uninstall"
# after_app_uninstall = "star_rentals.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "star_rentals.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"Vehicle Tyoe": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }
# doc_events = {
#     "*": {
#         "before_insert": "star_rentals.api.send_otp"
#     }
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#     "monthly": ["star_rentals.api.process_for_driver_payout"]
# }

# scheduler_events = {
#	"all": [
#		"star_rentals.tasks.all"
#	],
#	"daily": [
#		"star_rentals.tasks.daily"
#	],
#	"hourly": [
#		"star_rentals.tasks.hourly"
#	],
#	"weekly": [
#		"star_rentals.tasks.weekly"
#	],
#	"monthly": [
#		"star_rentals.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "star_rentals.install.before_tests"

# Overriding Methods
# ------------------------------
# #
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "star_rentals.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "star_rentals.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["star_rentals.utils.before_request"]
# after_request = ["star_rentals.utils.after_request"]

# Job Events
# ----------
# before_job = ["star_rentals.utils.before_job"]
# after_job = ["star_rentals.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"star_rentals.auth.validate"
# ]
