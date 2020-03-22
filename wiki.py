import requests
import json

#API = 'https://www.wikidata.org/w/api.php'
# for test wikidata
API = 'https://test.wikidata.org/w/api.php'
S = requests.Session()

#Ask for login token
def getLoginToken():	
	PARAMS = {
	    'action':"query",
	    'meta':"tokens",
	    'type':"login",
	    'format':"json"
	}
	R = S.get(url=API, params=PARAMS)
	DATA = R.json()
	LOGIN_TOKEN = DATA['query']['tokens']['logintoken']
	return LOGIN_TOKEN

# After get the login permits, use this token to login. 
def login(username, password, LOGIN_TOKEN):
	PARAMS = {
	    'action':"login",
	    'lgname':username,
	    'lgpassword':password,
	    'lgtoken':LOGIN_TOKEN,
	    'format':"json"
	}
	S.post(API, data=PARAMS)

# Get the edits token(key) which is used to have permission to edit. 
# The token return is used to in the following edit funcions.
def getEditToken():
	#ask for edit token
	PARAMS = {
	    'action':"query",
	    'meta':"tokens",
	    'type':"csrf",
	    'format':"json"
	}
	R = S.get(url=API, params=PARAMS)
	DATA = R.json()
	EDIT_TOKEN = DATA['query']['tokens']['csrftoken']
	return EDIT_TOKEN

#Create a new page, return ID("Q56676003") which can be used to create the page(each page has an id from wikidata org). 
def createPage(EDIT_TOKEN):
	PARAMS = {
		'action' : 'wbeditentity',
		'new' : "item",
		'data' : '{}',
		'token' : EDIT_TOKEN,
		'format' : 'json',
	}
	R = S.post(API, data = PARAMS)
	DATA = R.json()
	print DATA
	ID = DATA['entity']['id']
	# The ID return is the QID, such as "Q56676003" in each page.
	return ID

# Cannot be used currently, because the wiki account has low rank such as there is no permission to detele page.
# if keep the page empty, it can be detele by Administrator from Wikidate Org.
def deletePage(QID, EDIT_TOKEN):
	PARAMS = {
		"action": "delete",
		"format": "json",
		"title": QID,
		"token": EDIT_TOKEN
	}
	print PARAMS
	R = S.post(API, data = PARAMS)
	DATA = R.json()
	print(json.dumps(DATA, indent=4, sort_keys=True))

#Create the label and definition(IAO_0000115) for the each page.
# Does IAO_0000115 is fixed ?
def setLabel(lebal, QID, EDIT_TOKEN, description=None):
	if description:
		DATA = {
		    "labels":[{"language":"en","value":lebal}],
		    "descriptions":[{"language":"en","value":description}]
		}
	else:
		DATA = {
		    "labels":[{"language":"en","value":lebal}]
		}
	DATA = json.dumps(DATA) 
	PARAMS = {
	    'action' : 'wbeditentity',
	    'id' : QID,
	    'data' : DATA,
	    'token' : EDIT_TOKEN,
	    'format' : 'json'
	}
	R = S.post(API, data = PARAMS)
	DATA = R.json()
	print(json.dumps(DATA, indent=4, sort_keys=True))

def editLabel(lebal, QID, EDIT_TOKEN, description=None):
	if description:
		DATA = {
		    "labels":[{"language":"en","value":lebal}],
		    "descriptions":[{"language":"en","value":description}]
		}
	else:
		DATA = {
		    "labels":[{"language":"en","value":lebal}]
		}
	DATA = json.dumps(DATA) 
	PARAMS = {
	    'action' : 'wbeditentity',
	    'id' : QID,
	    'data' : DATA,
	    'token' : EDIT_TOKEN,
	    'format' : 'json'
	}
	R = S.post(API, data = PARAMS)
	DATA = R.json()
	try:
		if "error" in DATA:
			return DATA["error"]["messages"][0]["parameters"][2].split("|")[-1].replace("]]", "")
		else:
			return -1
	except:
		return -1

def get_property(qid, pid):
	QID = qid
	PARAMS_3 = {
	    'action' : 'wbgetclaims',
	    "entity" : QID,
	    'property' : pid
	}
	R = S.post(API, data = PARAMS_3)
	return R.text	

def set_definition(qid, EDIT_TOKEN, value, property):
	#create part of statement (only suport to reference to wikidata)
	QID = qid
	PARAMS_3 = {
	    'action' : 'wbcreateclaim',
	    "entity":QID,
	    'token' : EDIT_TOKEN,
	    'format' : 'json',
	    # for test wiki
	    'property' : property,
	    'snaktype' : 'value',
	    'value' : value
	}
	print PARAMS_3
	R = S.post(API, data = PARAMS_3)
	DATA = R.json()
	print(json.dumps(DATA, indent=4, sort_keys=True))

def set_part_of(qid, EDIT_TOKEN, p_qid, property):
	#create part of statement (only suport to reference to wikidata)
	QID = qid
	PARAMS_3 = {
	    'action' : 'wbcreateclaim',
	    "entity":QID,
	    'token' : EDIT_TOKEN,
	    'format' : 'json',
	    # for test wiki
	    'property' : property,
	    #'property' : 'P361',
	    'snaktype' : 'value',
	    'value' : "{'entity-type': 'item', 'numeric-id': '"+p_qid[1:]+"'}"
	}
	R = S.post(API, data = PARAMS_3)
	DATA = R.json()
	print(json.dumps(DATA, indent=4, sort_keys=True))

def set_has_part(qid, EDIT_TOKEN, p_qid, property):
	#create part of statement (only suport to reference to wikidata)
	QID = qid
	PARAMS_3 = {
	    'action' : 'wbcreateclaim',
	    "entity":QID,
	    'token' : EDIT_TOKEN,
	    'format' : 'json',
	    # for test wiki
	    'property' : property,
	    #'property' : 'P361',
	    'snaktype' : 'value',
	    'value' : "{'entity-type': 'item', 'numeric-id': '"+p_qid[1:]+"'}"
	}
	R = S.post(API, data = PARAMS_3)
	DATA = R.json()
	print(json.dumps(DATA, indent=4, sort_keys=True))

def set_synonym(qid, EDIT_TOKEN, value, property):
	#create part of statement (only suport to reference to wikidata)
	QID = qid
	PARAMS_3 = {
	    'action' : 'wbcreateclaim',
	    "entity":QID,
	    'token' : EDIT_TOKEN,
	    'format' : 'json',
	    # for test wiki
	    'property' : property,
	    'snaktype' : 'value',
	    'value' : value
	}
	print PARAMS_3
	R = S.post(API, data = PARAMS_3)
	DATA = R.json()
	print(json.dumps(DATA, indent=4, sort_keys=True))

def set_creation_date(qid, EDIT_TOKEN, value, property):
	#create part of statement (only suport to reference to wikidata)
	QID = qid
	PARAMS_3 = {
	    'action' : 'wbcreateclaim',
	    "entity":QID,
	    'token' : EDIT_TOKEN,
	    'format' : 'json',
	    # for test wiki
	    'property' : property,
	    'snaktype' : 'value',
	    'value' : value
	}
	#print PARAMS_3
	R = S.post(API, data = PARAMS_3)
	DATA = R.json()
	print(json.dumps(DATA, indent=4, sort_keys=True))

def set_comment(qid, EDIT_TOKEN, value, property):
	#create part of statement (only suport to reference to wikidata)
	QID = qid
	PARAMS_3 = {
	    'action' : 'wbcreateclaim',
	    "entity":QID,
	    'token' : EDIT_TOKEN,
	    'format' : 'json',
	    # for test wiki
	    'property' : property,
	    'snaktype' : 'value',
	    'value' : value
	}
	#print PARAMS_3
	R = S.post(API, data = PARAMS_3)
	DATA = R.json()
	print(json.dumps(DATA, indent=4, sort_keys=True))

def set_see_also(qid, EDIT_TOKEN, value, property):
	#create part of statement (only suport to reference to wikidata)
	QID = qid
	PARAMS_3 = {
	    'action' : 'wbcreateclaim',
	    "entity":QID,
	    'token' : EDIT_TOKEN,
	    'format' : 'json',
	    # for test wiki
	    'property' : property,
	    'snaktype' : 'value',
	    'value' : value
	}
	#print PARAMS_3
	R = S.post(API, data = PARAMS_3)
	DATA = R.json()
	print(json.dumps(DATA, indent=4, sort_keys=True))

def set_elucidation(qid, EDIT_TOKEN, value, property):
	#create part of statement (only suport to reference to wikidata)
	QID = qid
	PARAMS_3 = {
	    'action' : 'wbcreateclaim',
	    "entity":QID,
	    'token' : EDIT_TOKEN,
	    'format' : 'json',
	    # for test wiki
	    'property' : property,
	    'snaktype' : 'value',
	    'value' : value
	}
	#print PARAMS_3
	R = S.post(API, data = PARAMS_3)
	DATA = R.json()
	print(json.dumps(DATA, indent=4, sort_keys=True))

def set_measure(qid, EDIT_TOKEN, p_qid, property):
	#create part of statement (only suport to reference to wikidata)
	QID = qid
	PARAMS_3 = {
	    'action' : 'wbcreateclaim',
	    "entity":QID,
	    'token' : EDIT_TOKEN,
	    'format' : 'json',
	    # for test wiki
	    'property' : property,
	    #'property' : 'P361',
	    'snaktype' : 'value',
	    'value' : "{'entity-type': 'item', 'numeric-id': '"+p_qid[1:]+"'}"
	}
	R = S.post(API, data = PARAMS_3)
	DATA = R.json()
	print(json.dumps(DATA, indent=4, sort_keys=True))

def set_namespace(qid, EDIT_TOKEN, value, property):
	#create part of statement (only suport to reference to wikidata)
	QID = qid
	PARAMS_3 = {
	    'action' : 'wbcreateclaim',
	    "entity":QID,
	    'token' : EDIT_TOKEN,
	    'format' : 'json',
	    # for test wiki
	    'property' : property,
	    'snaktype' : 'value',
	    'value' : value
	}
	#print PARAMS_3
	print(PARAMS_3)
	R = S.post(API, data = PARAMS_3)
	DATA = R.json()
	print(json.dumps(DATA, indent=4, sort_keys=True))

def set_parent_item(qid, EDIT_TOKEN, p_qid, property):
	#create part of statement (only suport to reference to wikidata)
	QID = qid
	PARAMS_3 = {
	    'action' : 'wbcreateclaim',
	    "entity":QID,
	    'token' : EDIT_TOKEN,
	    'format' : 'json',
	    # for test wiki
	    'property' : property,
	    #'property' : 'P361',
	    'snaktype' : 'value',
	    'value' : "{'entity-type': 'item', 'numeric-id': '"+p_qid[1:]+"'}"
	}
	R = S.post(API, data = PARAMS_3)
	DATA = R.json()
	print(json.dumps(DATA, indent=4, sort_keys=True))