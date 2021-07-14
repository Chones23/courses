# -*- coding: utf-8 -*-
# Copyright (c) 2021, Nusantara Digital Konsultan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class TemplateGates(Document):
	def on_update(self):
		x = frappe.db.sql("""select count(name) as name from `tabTemplate Gates` where default_ndk= '1'""",as_dict=1)
		if x != [] :
			if x[0].name > 1 :
				frappe.msgprint(_('ada Template Gates lain yang Default'), raise_exception=1, indicator='red')
