#!/usr/bin/python
# -*- coding: utf-8 -*-

def filterTags(attrs):
	if not attrs: return
	tags={}
  
# Etiquetas fijas
	tags.update({'highway':'path'})
	tags.update({'cattle':'designated'})

# Nombre
	tags.update({'name':'x'})
	if attrs['ETIQUETA'] == "" or attrs['ETIQUETA'] == "S/N":
		del tags['name']
	else:
		tags ['name'] = attrs ['ETIQUETA']
	
# COMPO_0635 01=eje, 02=margen
	tags.update({'area':'xx'})
	if attrs['COMPO_0635'] == '01':
		del tags['name']
	elif attrs['COMPO_0635'] == '02':
		tags.update({'area':'yes'})
	else:
		del tags['area']	
		
	return tags
