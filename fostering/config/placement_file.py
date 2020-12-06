from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Key Information"),
			"items": [
				{
					"type": "doctype",
					"name": "Key Information",
				},
			]
		},
		{
			"label": _("Diary Record"),
			"items": [
				{
					"type": "doctype",
					"name": "Diary Record",
				},
			]
		},
{
			"label": _("Fostering Social Worker"),
			"items": [
				{
					"type": "doctype",
					"name": "Fostering Social Worker",
				},
			]
		},
{
			"label": _("Childs Social Worker"),
			"items": [
				{
					"type": "doctype",
					"name": "Childs Social Worker",
				},
			]
		},

		
	]