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

#upload title 
QID = 'Q56653953'
DATA = {
    "labels":[{"language":"en","value":"leaf"}],
    "descriptions":[{"language":"en","value":"Could put definition (IAO0000115) here"}]
}
DATA = json.dumps(DATA) 
PARAMS_2 = {
    'action' : 'wbeditentity',
    'id' : QID,
    'data' : DATA,
    'token' : EDIT_TOKEN,
    'format' : 'json'
}
R = S.post(API, data = PARAMS_2)
DATA = R.json()
#print(json.dumps(DATA, indent=4, sort_keys=True))

#create part of statement (only suport to reference to wikidata)
QID = 'Q56653953'
PARAMS_3 = {
    'action' : 'wbcreateclaim',
    "entity":QID,
    'token' : EDIT_TOKEN,
    'format' : 'json',
    'property' : 'P361',
    'snaktype' : 'novalue',
    #'value' : '{https://www.wikidata.org/wiki/Property:P361}'
}
R = S.post(API, data = PARAMS_3)
DATA = R.json()
print(json.dumps(DATA, indent=4, sort_keys=True))