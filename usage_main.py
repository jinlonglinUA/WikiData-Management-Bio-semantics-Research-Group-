import wiki
import property
import sys
import json
import collections
from os import listdir
from os.path import isfile, join

#used for test.wiki since: 
#As an anti-abuse measure, you are limited from performing this action too many times 
#in a short space of time, and you have exceeded this limit.
import time

login_token = wiki.getLoginToken()
wiki.login("CarexOntology","carex", login_token)
edit_token = wiki.getEditToken()

# wiki.get_property("Q181764")

# #create pages
# usage: python usage_main.py <path to txt directory> <qid_2019.csv> <test_qid.csv>
# data = collections.OrderedDict(sorted(property.get_label(sys.argv[1]).items()))
# with open(sys.argv[2], 'w') as f, open(sys.argv[3],'r') as g:
# 	_qid = [q.split(",")[0] for q in g]
# 	for label, description in data.iteritems():
# 		if(label not in _qid):
# 			print label
# 			page_id = wiki.createPage(edit_token)
# 			wiki.setLabel(label, page_id, edit_token, description)
# 			f.write("%s,%s\n" % (label, page_id))
# 			time.sleep(0.5)

# # add name space
# value="http://biosemantics.arizona.edu/ontologies/carex"
# value = str('"' + value + '"')
# data = collections.OrderedDict(sorted(property.getQID(sys.argv[2]).items()))
# for label in data:
# 	Qid = data[label]
# 	wiki.set_namespace(Qid, edit_token, value, 'P82189')
# 	time.sleep(0.5)

# #add part of
# #usage: python usage.py <path to txt directory> <test_qid.csv>
# data = collections.OrderedDict(sorted(property.get_part_of(sys.argv[1], sys.argv[2]).items()))
# data = collections.OrderedDict(sorted(property.get_part_of_2(sys.argv[1], sys.argv[2]).items()))
# for label in data:
# 	print label
# 	# info = data[label]
# 	# Qid = info['QID']
# 	# partof = info['partof']
# 	# for p_qid in partof:
# 	# 	wiki.set_part_of(Qid, edit_token, p_qid, 'P791')
# 	# 	time.sleep(0.5)

# #add has part
# data = collections.OrderedDict(sorted(property.get_has_part(sys.argv[1], sys.argv[2]).items()))
# for label in data:
# 	info = data[label]
# 	Qid = info['QID']
# 	haspart = info['haspart']
# 	for p_qid in haspart:
# 		wiki.set_has_part(Qid, edit_token, p_qid, 'P81880')
# 		time.sleep(0.5)
# 	print label

# # add broad_synonym
# data = collections.OrderedDict(sorted(property.get_broad_synonym(sys.argv[1], sys.argv[2]).items()))
# for label in data:
# 	info = data[label]
# 	Qid = info['QID']
# 	broadsynonym = info['broadsynonym']
# 	#print label, broadsynonym
# 	for value in broadsynonym:
# 		value = str('"' + value + '"')
# 		wiki.set_synonym(Qid, edit_token, value, 'P81607')
# 		time.sleep(0.5)
# 	print label

# # add exact_synonym
# data = collections.OrderedDict(sorted(property.get_exact_synonym(sys.argv[1], sys.argv[2]).items()))
# for label in data:
# 	info = data[label]
# 	Qid = info['QID']
# 	exactsynonym = info['exactsynonym']
# 	#print label, broadsynonym
# 	for value in exactsynonym:
# 		value = str('"' + value + '"')
# 		wiki.set_synonym(Qid, edit_token, value, 'P82002')
# 		time.sleep(0.5)
# 	print label

# # add creation_date
# data = collections.OrderedDict(sorted(property.get_creation_date(sys.argv[1], sys.argv[2]).items()))
# for label in data:
# 	info = data[label]
# 	Qid = info['QID']
# 	creationdate = info['creationdate']
# 	#print label, broadsynonym
# 	for value in creationdate:
# 		value = str('"' + value + '"')
# 		wiki.set_creation_date(Qid, edit_token, value, 'P81998')
# 		time.sleep(0.5)
# 	print label

# # add comment
# data = collections.OrderedDict(sorted(property.get_comment(sys.argv[1], sys.argv[2]).items()))
# for label in data:
# 	info = data[label]
# 	Qid = info['QID']
# 	comment = info['comment']
# 	#print label, broadsynonym
# 	for value in comment:
# 		value = str('"' + value + '"')
# 		wiki.set_comment(Qid, edit_token, value, 'P82004')
# 		time.sleep(0.5)
# 	print label

# # add see also
# data = collections.OrderedDict(sorted(property.get_see_also(sys.argv[1], sys.argv[2]).items()))
# for label in data:
# 	info = data[label]
# 	Qid = info['QID']
# 	seealso = info['seealso']
# 	#print label, broadsynonym
# 	for value in seealso:
# 		value = str('"' + value + '"')
# 		wiki.set_see_also(Qid, edit_token, value, 'P82005')
# 		time.sleep(0.5)
# 	print label

# # add id
# data = collections.OrderedDict(sorted(property.get_id(sys.argv[1], sys.argv[2]).items()))
# for label in data:
# 	info = data[label]
# 	Qid = info['QID']
# 	id = info['id']
# 	#print label, broadsynonym
# 	for value in id:
# 		value = str('"' + value + '"')
# 		wiki.set_id(Qid, edit_token, value, 'P82003')
# 		time.sleep(0.5)
# 	print label

# # add definition_source
# data = collections.OrderedDict(sorted(property.get_definition_source(sys.argv[1], sys.argv[2]).items()))
# for label in data:
# 	info = data[label]
# 	Qid = info['QID']
# 	definitionsource = info['definitionsource']
# 	#print label, broadsynonym
# 	for value in definitionsource:
# 		value = str('"' + value + '"')
# 		wiki.set_definition_source(Qid, edit_token, value, 'P82000')
# 		time.sleep(0.5)
# 	print label

# # add elucidation
# data = collections.OrderedDict(sorted(property.get_elucidation(sys.argv[1], sys.argv[2]).items()))
# for label in data:
# 	info = data[label]
# 	Qid = info['QID']
# 	elucidation = info['elucidation']
# 	#print label, broadsynonym
# 	for value in elucidation:
# 		wiki.set_elucidation(Qid, edit_token, value, 'P81999')
# 		time.sleep(0.5)
# 	print label

# # add exclude measure
# data = collections.OrderedDict(sorted(property.get_measured_exclude(sys.argv[1], sys.argv[2]).items()))
# for label in data:
# 	info = data[label]
# 	Qid = info['QID']
# 	measuredexclude = info['measuredexclude']
# 	#print label, broadsynonym
# 	for value in measuredexclude:
# 		wiki.set_measure(Qid, edit_token, value, 'P81996')
# 		time.sleep(0.5)
# 	print label

# # add include measure
# data = collections.OrderedDict(sorted(property.get_measured_include(sys.argv[1], sys.argv[2]).items()))
# for label in data:
# 	info = data[label]
# 	Qid = info['QID']
# 	measuredinclude = info['measuredinclude']
# 	#print label, broadsynonym
# 	for value in measuredinclude:
# 		wiki.set_measure(Qid, edit_token, value, 'P81997')
# 		time.sleep(0.5)
# 	print label

# # add definition
# data = collections.OrderedDict(sorted(property.get_definition(sys.argv[1], sys.argv[2]).items()))
# for label in data:
# 	print label
# 	content = wiki.get_property(data[label]['QID'], 'P88344')
# 	if data[label]['definition'] in content:
# 		continue
# 	elif data[label]['definition'] == '':
# 		continue
# 	else:
# 		info = data[label]
# 		Qid = info['QID']
# 		definition = info['definition']
# 		try:
# 			if not definition[0] == '"':
# 				value = str('"' + definition + '"')
# 			else:
# 				value = definition
# 			wiki.set_definition(Qid, edit_token, value, 'P88344')
# 			exit()
# 		except:
# 			continue
# 		time.sleep(0.5)

# # add parent_item
# data = collections.OrderedDict(sorted(property.get_parents(sys.argv[1], sys.argv[2]).items()))
# for label in data:
# 	print label
# 	if label <= 'acute-rounded':
# 		continue
# 	else :
# 		info = data[label]
# 		Qid = info['QID']
# 		parment = info['parentTerm']
# 		for p_qid in parment:
# 			wiki.set_parent_item(Qid, edit_token, p_qid, 'P88347')
# 			time.sleep(0.5)
	
