#!/usr/bin/python
# -*- coding: utf-8 -*-

def filterTags(attrs):
	if not attrs: return

	tags={}

# Etiquetas fijas
	tags.update({'natural':'water'})
	tags.update({'water':'reservoir'})

# Conversión de etiquetas
# Nombre
	tags.update({'name':'x'})
	if attrs['ETIQUETA'] == "" or attrs['ETIQUETA'] == "S/N":
		del tags['name']
	else:
		tags ['name'] = attrs ['ETIQUETA']
	
#Régimen hídrico. REGIM_0316
	tags.update({'intermittent':'xxx'})
	if attrs['REGIM_0316'] != '1':
		tags.update({'intermittent':'yes'})
	else:
		tags.update({'intermittent':'no'})
#Salinidad. TIPO_0316
	tags.update({'salt':'xx'})
	if attrs['TIPO_0316'] == '01':
		tags.update({'salt':'no'})
	elif attrs['TIPO_0316'] == '02':
		tags.update({'salt':'yes'})
	else:
		del tags['salt']	
		
	return tags

