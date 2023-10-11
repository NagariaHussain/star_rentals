# Copyright (c) 2023, Hussain and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
		{"label": "Make", "fieldname": "make", "fieldtype": "Data", "width": 200},
		{"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency"},
	]

	bookings = frappe.get_all(
		"Ride Booking", 
		fields=["make", "total_amount"], 
		filters={"docstatus":1}
	)

	revenue_by_make = {}
	for booking in bookings:
		if booking.make in revenue_by_make:
			revenue_by_make[booking.make] += booking.total_amount
		else:
			revenue_by_make[booking.make] = booking.total_amount

	# BMW: 4000, Hyundai: 100 => 
	# {"make": "BMW", "revenue": 4000}

	data = [
		{"make": make, "revenue": revenue} 
		for make, revenue in revenue_by_make.items()
	]

	chart = {
		"type": "pie",
		"data": {
			"labels": [d["make"] for d in data],
			"datasets": [
				{
					"values": [d["revenue"] for d in data]
				}
			]
		}
	}

	summary =  [
		{
			"value": sum(d["revenue"] for d in data),
			"label": "Total Revenue",
			"indicator": "green",
			"datatype": "Currency"
		}
	]
	return columns, data, "Something", chart, summary
