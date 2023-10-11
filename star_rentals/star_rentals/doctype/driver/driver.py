# Copyright (c) 2023, Hussain and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Driver(Document):
	def before_save(self):
		if not self.last_name:
			self.full_name = self.first_name
		else:
			self.full_name = self.first_name + " " + self.last_name

	def on_trash(self):
		if self.name in [jhgf]:
			frappe.throw("You can't delete a driver")