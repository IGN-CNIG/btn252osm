#!/usr/bin/python
# -*- coding: utf-8 -*-

def filterTags(attrs):
	if not attrs: return

	tags={}

# Etiquetas conversión
		
	
# Tipo de Surgencia de agua. (01 Fuente, 02 Manantial, 03 Pozo)
	tags.update({'natural':'x'})
	tags.update({'man_made':'x'})
	if attrs['TIPO_0334'] == '01' or attrs['TIPO_0334'] =='02':
		tags.update({'natural':'spring'})
	else:
		tags.update({'man_made':'water_well'})
	
	if attrs['TIPO_0334'] == '01' or attrs['TIPO_0334'] =='02':
		del tags ['man_made']
	else:	
		del tags ['natural']

# Nombre
	tags.update({'name':'x'})
	if attrs['ETIQUETA'] == "":
		del tags['name']
	else:
		tags ['name'] = attrs ['ETIQUETA']

		

	return tags

