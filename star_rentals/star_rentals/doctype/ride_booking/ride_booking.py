# Copyright (c) 2023, Hussain and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self):
		self.set_total_amount()
	
	def set_total_amount(self):
		total_amount = 0

		rate = self.rate or frappe.get_single("Rental Settings").default_price_per_km
		for item in self.items:
			item.amount = item.distance * rate
			total_amount += item.amount
		
		self.total_amount = total_amount


