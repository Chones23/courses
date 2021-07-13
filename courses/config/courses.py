from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
        {
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Human Design Beta Ver",
					"description": _("Human Design Beta Ver")
				},
				{
					"type": "doctype",
					"name": "Template Gates",
					"description": _("Template Gates")
				},
				{
					"type": "doctype",
					"name": "Template Channel",
					"description": _("Template Channel")
				},
				{
					"type": "doctype",
					"name": "The Gates",
					"description": _("The Gates")
				},
				{
					"type": "doctype",
					"name": "The Channel",
					"description": _("The Channel")
				},
			]
		},

	]
