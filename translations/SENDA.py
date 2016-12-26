#!/usr/bin/python
# -*- coding: utf-8 -*-

def filterTags(attrs):
	if not attrs: return

	tags={}
	tags.update({'highway':'track'})
# Nombre
	tags.update({'name':'x'})
	if attrs['ETIQUETA'] == "":
		del tags['name']
	else:
		tags ['name'] = attrs ['ETIQUETA']

# Situación SITUA_0610 (subterránea, superficial, elevada)
	tags.update({'layer':'x'})
	if attrs['SITUA_0610'] == '01':
		tags.update({'layer':'-1'})
	elif attrs['SITUA_0610'] == '02':
                del tags['layer']
#		tags.update({'layer':'0'})
	elif attrs['SITUA_0610'] == '03':
		tags.update({'layer':'1'})

	return tags
