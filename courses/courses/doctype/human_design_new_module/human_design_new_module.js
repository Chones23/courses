// Copyright (c) 2021, Nusantara Digital Konsultan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Human Design New Module', {
	template_gates: function(frm) {
		frm.clear_table("gates")

		if(frm.doc.template_gates == undefined){
			frm.clear_table("gates")
			frm.refresh_field("gates");
		}

		if(frm.doc.template_gates){
			frappe.call({
	      method:"courses.courses.doctype.human_design_new_module.human_design_new_module.gate_temp",
	      args:{template_gates:frm.doc.template_gates},
	      callback:function(r){
	        if(r.message){
	          $.each(r.message, function(i,d){
	            var row = frm.add_child("gates");
							row.link_gate= d.link_gate,
							row.read= d.read
	          });
	        };
	        frm.refresh_field("gates");
	      }
	    })
		}
	},
	template_channel: function(frm) {
		frm.clear_table("channel")

		if(frm.doc.template_channel == undefined){
			frm.clear_table("channel")
			frm.refresh_field("channel");
		}

		if(frm.doc.template_channel){
			frappe.call({
	      method:"courses.courses.doctype.human_design_new_module.human_design_new_module.chanel_temp",
	      args:{template_channel:frm.doc.template_channel},
	      callback:function(r){
	        if(r.message){
	          $.each(r.message, function(i,d){
	            var row = frm.add_child("channel");
							row.link_channel= d.link_channel,
							row.read= d.read
	          });
	        };
	        frm.refresh_field("channel");
	      }
	    })
		}
	},
	onload: function(frm){
		if(frm.doc.__islocal){
			frappe.call({
				method: "courses.courses.doctype.human_design_new_module.human_design_new_module.get_default_gate",
				callback: function(data) {
					if(data.message){
						frappe.model.set_value(frm.doctype,frm.docname, "template_gates", data.message);
					}
				}
			});
			frappe.call({
				method: "courses.courses.doctype.human_design_new_module.human_design_new_module.get_default_channel",
				callback: function(data) {
					if(data.message){
						frappe.model.set_value(frm.doctype,frm.docname, "template_channel", data.message);
					}
				}
			});
		}
	}
});
