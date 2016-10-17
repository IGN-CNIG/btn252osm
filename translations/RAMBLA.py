#!/usr/bin/python
# -*- coding: utf-8 -*-

def filterTags(attrs):
	if not attrs: return

	tags={}
	tags.update({'waterway':'stream'})
	tags.update({'intermittent':'yes'})
# Nombre
	tags.update({'name':'x'})
	if attrs['ETIQUETA'] == "":
		del tags['name']
	else:
		tags ['name'] = attrs ['ETIQUETA']
	
	return tags

