# The wiki_search.py is used to search the sources from wikidate.
import requests
import json
import sys

API = 'https://www.wikidata.org/w/api.php'
query = 'apple' if len(sys.argv) != 2 else sys.argv[1] 

params = {
	'action' : 'wbsearchentities',
	'format' : 'json',
	'language' : 'en',
	'search' : query #modiy this tuple for other actions
}

#https://www.wikidata.org/w/api.php?action=wbsetdescription&id=Q42&language=en&value=An%20encyclopedia%20that%20everyone%20can%20edit
'''
params = {
	'action' : 'wbsetdescription',
	'id' : 'Q42',
	'format' : 'json',
	'language' : 'en',
	'value' : An%20encyclopedia%20that%20everyone%20can%20edit
}
'''

r = requests.get(API, params = params)

print("Wikidata web sourse:")
print(json.dumps(r.json(), indent=4, sort_keys=True))

print("\n\nAll item (%s) description on Wikidata:" % query)
print(json.dumps([d['description'] for d in r.json()['search']], indent=4, sort_keys=True))

print(json.dumps(r.json()['search'][4]['description'], indent=4, sort_keys=True))