from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'Key Information',
		'non_standard_fieldnames': {
			'Diary Record': 'party_name',
		},
		'dynamic_links': {
			'party_name': ['Key Information', 'Key Information']
		},
		'transactions': [
			{
				'items': ['Diary Record']
			},
		]
	}