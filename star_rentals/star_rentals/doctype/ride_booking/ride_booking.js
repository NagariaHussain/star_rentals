// Copyright (c) 2023, Hussain and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
	refresh(frm) {
        frm.set_query("vehicle", () => {
            return {
                filters: {
                    "status": "Active"
                }
            }
        })
	},
});
