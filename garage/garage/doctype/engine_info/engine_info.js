// Copyright (c) 2018, crisco and contributors
// For license information, please see license.txt

frappe.ui.form.on('Engine Info', {
	refresh: function(frm) {
		this.frm.set_indicator('Engine Info',
			function(doc) { return  "green" })

	}
});
