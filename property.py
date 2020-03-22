### Created by Jinlong Lin
### My personal main page https://www2.cs.arizona.edu/~jinlonglin/
###  Bio-semantics Research Group is led by Professor Hong Cui

import sys
import json
from os import listdir
from os.path import isfile, join

def getFiles(path):
	return [join(path, f) for f in listdir(path) if isfile(join(path, f)) and 'txt' in f]

def getQID(path):
	QID = {}
	with open(path, 'r') as f:
		for line in f:
			line = line.strip().split(',')
			QID[line[0]] = line[-1]
	return QID

def get_label(path):
	files = getFiles(path)
	data = {}
	for file in files:
		with open(file, 'r') as fr:
			info = json.load(fr)
			try:
				label = info['entries'][0]['term']
			except:
				continue
			data[label] = None
			try:
				resultAnnotations = info['entries'][0]['resultAnnotations']
				#print resultAnnotations
				for term in resultAnnotations:
					if 'IAO_0000115' in term['property']:
						data[label] = term['value']
			except:
				pass 
	return data

def get_definition(path, qid_file):
	files = getFiles(path)
	qid = getQID(qid_file)
	data = {}
	for file in files:
	 	with open(file, 'r') as fr:
	 		info = json.load(fr)
	 		try:
	 			label = info['entries'][0]['term']
	 		except:
	 			continue
	 		#data[label] = None
	 		try:
				resultAnnotations = info['entries'][0]['resultAnnotations']
				#print resultAnnotations
				for term in resultAnnotations:
					if 'IAO_0000115' in term['property']:
						data[label] = {}
						data[label]['QID'] = qid[label]
						data[label]['definition'] = term['value']
			except:
				continue
	return data

def get_part_of(path, qid_file):
	files = getFiles(path)
	qid = getQID(qid_file)
	data = {}
	for file in files:
		with open(file, 'r') as fr:
			info = json.load(fr)
			try:
				label = info['entries'][0]['term']
			except:
				continue
			data[label] = {}
			data[label]['partof'] = []
			print qid
			data[label]['QID'] = qid[label]
			try:
				resultAnnotations = info['entries'][0]['resultAnnotations']
				for term in resultAnnotations:
					if term['property'] == 'part of':
						key = term['value'].split('carex#')[-1]
						key = key.replace('_', ' ')
						data[label]['partof'].append(qid[key])						
			except:
				pass 
	return data

def get_part_of_2(path, qid_file):
	files = getFiles(path)
	qid = getQID(qid_file)
	data = {}
	for file in files:
		with open(file, 'r') as fr:
			info = json.load(fr)
			try:
				label = info['entries'][0]['term']
			except:
				continue
			data[label] = {}
			data[label]['partof'] = []
			data[label]['QID'] = qid[label]
			try:
				resultAnnotations = info['entries'][0]['resultAnnotations']
				for term in resultAnnotations:
					if 'BFO_0000050' in term['property']:
						key = term['value'].split('carex#')[-1]
						key = key.replace('_', ' ')
						key = key.replace('%20', ' ')
						data[label]['partof'].append(qid[key])						
			except:
				pass 
	return data

def get_has_part(path, qid_file):
	files = getFiles(path)
	qid = getQID(qid_file)
	data = {}
	for file in files:
		with open(file, 'r') as fr:
			info = json.load(fr)
			try:
				label = info['entries'][0]['term']
			except:
				continue
			data[label] = {}
			data[label]['haspart'] = []
			data[label]['QID'] = qid[label]
			try:
				resultAnnotations = info['entries'][0]['resultAnnotations']
				#print resultAnnotations
				for term in resultAnnotations:
					if term['property'] == 'has part':
						key = term['value'].split('carex#')[-1]
						key = key.replace('%20', ' ')
						data[label]['haspart'].append(qid[key])
			except:
				pass 
	return data

def get_broad_synonym(path, qid_file):
	files = getFiles(path)
	qid = getQID(qid_file)
	data = {}
	for file in files:
		with open(file, 'r') as fr:
			info = json.load(fr)
			try:
				label = info['entries'][0]['term']
			except:
				continue
			data[label] = {}
			data[label]['broadsynonym'] = []
			data[label]['QID'] = qid[label]
			try:
				resultAnnotations = info['entries'][0]['resultAnnotations']
				#print resultAnnotations
				for term in resultAnnotations:
					if 'BroadSynonym' in term['property']:
						value = term['value']
						data[label]['broadsynonym'].append(value)
			except:
				pass 
	return data

def get_exact_synonym(path, qid_file):
	files = getFiles(path)
	qid = getQID(qid_file)
	data = {}
	for file in files:
		with open(file, 'r') as fr:
			info = json.load(fr)
			try:
				label = info['entries'][0]['term']
			except:
				continue
			data[label] = {}
			data[label]['exactsynonym'] = []
			data[label]['QID'] = qid[label]
			try:
				resultAnnotations = info['entries'][0]['resultAnnotations']
				#print resultAnnotations
				for term in resultAnnotations:
					if 'hasExactSynonym' in term['property']:
						value = term['value']
						data[label]['exactsynonym'].append(value)
			except:
				pass 
	return data

def get_creation_date(path, qid_file):
	files = getFiles(path)
	qid = getQID(qid_file)
	data = {}
	for file in files:
		with open(file, 'r') as fr:
			info = json.load(fr)
			try:
				label = info['entries'][0]['term']
			except:
				continue
			data[label] = {}
			data[label]['creationdate'] = []
			data[label]['QID'] = qid[label]
			try:
				resultAnnotations = info['entries'][0]['resultAnnotations']
				#print resultAnnotations
				for term in resultAnnotations:
					if 'creation_date' in term['property']:
						value = term['value']
						data[label]['creationdate'].append(value)
			except:
				pass 
	return data

def get_comment(path, qid_file):
	files = getFiles(path)
	qid = getQID(qid_file)
	data = {}
	for file in files:
		with open(file, 'r') as fr:
			info = json.load(fr)
			try:
				label = info['entries'][0]['term']
			except:
				continue
			data[label] = {}
			data[label]['comment'] = []
			data[label]['QID'] = qid[label]
			try:
				resultAnnotations = info['entries'][0]['resultAnnotations']
				#print resultAnnotations
				for term in resultAnnotations:
					if 'comment' in term['property']:
						value = term['value']
						data[label]['comment'].append(value)
			except:
				pass 
	return data

def get_see_also(path, qid_file):
	files = getFiles(path)
	qid = getQID(qid_file)
	data = {}
	for file in files:
		with open(file, 'r') as fr:
			info = json.load(fr)
			try:
				label = info['entries'][0]['term']
			except:
				continue
			data[label] = {}
			data[label]['seealso'] = []
			data[label]['QID'] = qid[label]
			try:
				resultAnnotations = info['entries'][0]['resultAnnotations']
				#print resultAnnotations
				for term in resultAnnotations:
					if 'seeAlso' in term['property']:
						value = term['value']
						data[label]['seealso'].append(value)
			except:
				pass 
	return data

def get_id(path, qid_file):
	files = getFiles(path)
	qid = getQID(qid_file)
	data = {}
	for file in files:
		with open(file, 'r') as fr:
			info = json.load(fr)
			try:
				label = info['entries'][0]['term']
			except:
				continue
			data[label] = {}
			data[label]['id'] = []
			data[label]['QID'] = qid[label]
			try:
				resultAnnotations = info['entries'][0]['resultAnnotations']
				#print resultAnnotations
				for term in resultAnnotations:
					if 'oboInOwl#id' in term['property']:
						value = term['value']
						data[label]['id'].append(value)
			except:
				pass 
	return data

def get_definition_source(path, qid_file):
	files = getFiles(path)
	qid = getQID(qid_file)
	data = {}
	for file in files:
		with open(file, 'r') as fr:
			info = json.load(fr)
			try:
				label = info['entries'][0]['term']
			except:
				continue
			data[label] = {}
			data[label]['definitionsource'] = []
			data[label]['QID'] = qid[label]
			try:
				resultAnnotations = info['entries'][0]['resultAnnotations']
				#print resultAnnotations
				for term in resultAnnotations:
					if 'IAO_0000119' in term['property']:
						value = term['value']
						data[label]['definitionsource'].append(value)
			except:
				pass 
	return data

def get_definition_source(path, qid_file):
	files = getFiles(path)
	qid = getQID(qid_file)
	data = {}
	for file in files:
		with open(file, 'r') as fr:
			info = json.load(fr)
			try:
				label = info['entries'][0]['term']
			except:
				continue
			data[label] = {}
			data[label]['definitionsource'] = []
			data[label]['QID'] = qid[label]
			try:
				resultAnnotations = info['entries'][0]['resultAnnotations']
				#print resultAnnotations
				for term in resultAnnotations:
					if 'IAO_0000119' in term['property']:
						value = term['value']
						data[label]['definitionsource'].append(value)
			except:
				pass 
	return data

def get_elucidation(path, qid_file):
	files = getFiles(path)
	qid = getQID(qid_file)
	data = {}
	for file in files:
		with open(file, 'r') as fr:
			info = json.load(fr)
			try:
				label = info['entries'][0]['term']
			except:
				continue
			data[label] = {}
			data[label]['elucidation'] = []
			data[label]['QID'] = qid[label]
			try:
				resultAnnotations = info['entries'][0]['resultAnnotations']
				#print resultAnnotations
				for term in resultAnnotations:
					if 'elucidation' in term['property']:
						value = term['value']
						data[label]['elucidation'].append(value)
			except:
				pass 
	return data

def get_measured_exclude(path, qid_file):
	files = getFiles(path)
	qid = getQID(qid_file)
	data = {}
	for file in files:
		with open(file, 'r') as fr:
			info = json.load(fr)
			try:
				label = info['entries'][0]['term']
			except:
				continue
			data[label] = {}
			data[label]['measuredexclude'] = []
			data[label]['QID'] = qid[label]
			try:
				resultAnnotations = info['entries'][0]['resultAnnotations']
				#print resultAnnotations
				for term in resultAnnotations:
					if 'measured-exclude' in term['property']:
						value = term['value']
						key = value.split("carex#")[1].replace('%20', ' ')
						data[label]['measuredexclude'].append(qid[key])
			except:
				pass 
	return data

def get_measured_include(path, qid_file):
	files = getFiles(path)
	qid = getQID(qid_file)
	data = {}
	for file in files:
		with open(file, 'r') as fr:
			info = json.load(fr)
			try:
				label = info['entries'][0]['term']
			except:
				continue
			data[label] = {}
			data[label]['measuredinclude'] = []
			data[label]['QID'] = qid[label]
			try:
				resultAnnotations = info['entries'][0]['resultAnnotations']
				#print resultAnnotations
				for term in resultAnnotations:
					if 'measured-include' in term['property']:
						value = term['value']
						key = value.split("carex#")[1].replace('%20', ' ')
						data[label]['measuredinclude'].append(qid[key])
			except:
				pass 
	return data

def get_parents(path, qid_file):
	files = getFiles(path)
	qid = getQID(qid_file)
	data = {}
	for file in files:
		with open(file, 'r') as fr:
			info = json.load(fr)
			try:
				label = info['entries'][0]['term']
			except:
				continue
			data[label] = {}
			data[label]['QID'] = qid[label]
			data[label]['parentTerm'] = []
			try:
				for term in info['entries'][0]['parentTerm'].split(';'):
					data[label]['parentTerm'].append(qid[term])
			except:
				pass 
	return data	



