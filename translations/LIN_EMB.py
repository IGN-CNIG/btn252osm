#!/usr/bin/python
# -*- coding: utf-8 -*-

def filterTags(attrs):
	if not attrs: return

	tags={}

# Etiquetas fijas
	tags.update({'natural':'water'})
	tags.update({'water':'reservoir'})

# Etiquetas conversión
# Nombre
	tags.update({'name':'x'})
	if attrs['ETIQUETA'] == "":
		del tags['name']
	else:
		tags ['name'] = attrs ['ETIQUETA']

	return tags

