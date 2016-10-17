#!/usr/bin/python
# -*- coding: utf-8 -*-

def filterTags(attrs):
	if not attrs: return

	tags={}

# Etiquetas fijas
	
	tags.update({'man_made':'reservoir_covered'})
	

# Etiquetas conversión
		
	
# Situación del depósito. SITUA_0331
	tags.update({'layer':'x'})
	if attrs['SITUA_0331'] == '01':
		tags.update({'layer':'-1'})
	elif attrs['SITUA_0331'] == '00':
		tags.update({'layer':'0'})
	elif attrs['SITUA_0331'] == '02':
		tags.update({'layer':'1'})

		

	return tags

