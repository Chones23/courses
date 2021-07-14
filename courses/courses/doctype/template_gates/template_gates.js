// Copyright (c) 2021, Nusantara Digital Konsultan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Template Gates', {
	default_ndk: function(frm) {
		frm.set_value('disabled',0)
	},
	disabled: function(frm) {
		frm.set_value('default_ndk',0)
	}
});

frappe.ui.form.on('Template Gate Item', {
	gates: function(frm, cdt, cdn) {
		var d = locals[cdt][cdn]
		var pos=0
		$.each(frm.doc.items, function(i, j) {
			if(d.gates == j.gates) {
				pos=pos+1
				if(pos>1) {
					frappe.msgprint(d.gates + " sudah ada");
					frappe.model.set_value(cdt, cdn, "gates","");
					frappe.model.set_value(cdt, cdn, "text_editor_1","");
				}
			}
		});
	}
});
