// Copyright (c) 2023, Hussain and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
	refresh(frm) {
        if (frm.doc.status != "Accepted") {
            frm.add_custom_button("Accept", () => {
                // show a dialog, ask for driver
                const dialog = new frappe.ui.Dialog({
                    title: "Assign Driver",
                    primary_action_label: "Create Booking",
                    fields: [
                        {
                            "label": "Driver",
                            "fieldtype": "Link",
                            "options": "Driver",
                            "fieldname": "driver",
                            "reqd": 1
                        }
                    ],
                    primary_action: (data) => {
                        console.log(data);
                        frappe.new_doc("Ride Booking", {
                            "vehicle": frm.doc.vehicle,
                            "driver": data.driver,
                            "status": "Booked"
                        })

                        frm.set_value("status", "Accepted");
                        frm.save();
                    }
                })

                dialog.show();
                // on click of a button, create a Ride Booking
                // take the  user to ride booking form

                
            });
        }

        if (frm.doc.status != "Rejected") {
            frm.add_custom_button("Reject", () => {
                frm.set_value("status", "Rejected");
                frm.save();
            });
        }
	},

});

