# Copyright (c) 2023, Hussain and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDriver(FrappeTestCase):
	def test_full_name_is_set_automatically(self):
		test_driver = frappe.new_doc("Driver")
		test_driver.first_name = "John"
		test_driver.last_name = "Doe"
		test_driver.dob = "2000-03-03"

		test_driver.insert()

		self.assertEqual(test_driver.full_name, "John Doe")

	def test_full_name_is_set_automatically_without_lastname(self):
		test_driver = frappe.new_doc("Driver")
		test_driver.first_name = "John"
		test_driver.dob = "2000-03-03"

		test_driver.insert()
		self.assertEqual(test_driver.full_name, "John")
