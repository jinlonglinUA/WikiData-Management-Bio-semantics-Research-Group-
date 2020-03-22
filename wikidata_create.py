import requests
import json
import sys

API = 'https://www.wikidata.org/w/api.php'
S = requests.Session()

#ask for login Token
PARAMS_0 = {
    'action':"query",
    'meta':"tokens",
    'type':"login",
    'format':"json"
}
R = S.get(url=API, params=PARAMS_0)
DATA = R.json()
LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

#login
PARAMS_0 = {
    'action':"login",
    'lgname':"CarexOntology",
    'lgpassword':"carex",
    'lgtoken':LOGIN_TOKEN,
    'format':"json"
}
R = S.post(API, data=PARAMS_0)

#ask for edit token
PARAMS_1 = {
    'action':"query",
    'meta':"tokens",
    'type':"csrf",
    'format':"json"
}
R = S.get(url=API, params=PARAMS_1)
DATA = R.json()
EDIT_TOKEN = DATA['query']['tokens']['csrftoken']

# create id
PARAMS_2 = {
	'action' : 'wbeditentity',
	'new' : "item",
	'data' : '{}',
	'token' : EDIT_TOKEN,
	'format' : 'json',
}
R = S.post(API, data = PARAMS_2)
DATA = R.json()
ID = DATA['entity']['id']
print("created an empty entity with id: " + ID)
