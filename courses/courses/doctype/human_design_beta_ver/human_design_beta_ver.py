# -*- coding: utf-8 -*-
# Copyright (c) 2021, Nusantara Digital Konsultan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class HumanDesignBetaVer(Document):
	pass

@frappe.whitelist()
def get_default_gate():
	def_pl = frappe.db.get_value("Template Gates",{"disabled":0,"default_ndk":1},"name")
	if def_pl not in ['' or None]:
		return def_pl

@frappe.whitelist()
def get_default_channel():
	def_pl = frappe.db.get_value("Template Channel",{"disabled":0,"default_ndk":1},"name")
	if def_pl not in ['' or None]:
		return def_pl

@frappe.whitelist()
def gate_temp(template_gates):
	row = frappe.db.sql("""Select gates, text_editor_1
					 from `tabTemplate Gate Item`
					 where parent = %s
					 order by gates asc""",template_gates,as_dict=1)

	si_list = []
	for i in row :
		si_list.append(frappe._dict({
			"link_gate": i.gates,
			"read": i.text_editor_1
		}))
	return si_list

@frappe.whitelist()
def chanel_temp(template_channel):
	row = frappe.db.sql("""Select channel, text_editor_1
					 from `tabTemplate Channel Item`
					 where parent = %s
					 order by channel asc""",template_channel,as_dict=1)

	si_list = []
	for i in row :
		si_list.append(frappe._dict({
			"link_channel": i.channel,
			"read": i.text_editor_1
		}))
	return si_list
