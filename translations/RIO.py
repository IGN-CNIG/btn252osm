#!/usr/bin/python
# -*- coding: utf-8 -*-

def filterTags(attrs):
	if not attrs: return

	tags={}

# Nombre
	tags.update({'name':'x'})
	if attrs['ETIQUETA'] == "":
		del tags['name']
	else:
		tags ['name'] = attrs ['ETIQUETA']

#Régimen hidrico. REGIM_0316
	tags.update({'intermittent':'x'})
	if attrs['REGIM_0301'] == '01':
		tags.update({'intermittent':'no'})
	else:
		tags.update({'intermittent':'yes'})
		
#Categorias. Se clasifican por longitud. En realidad no se corresponde con la definición de arroyo y río de OpenStreetMap.
#01 Primera, Tajo, Guadiana, etc
#02 Segunda, > 90km excluidos los de primera.
#07 Tercera (>40>90) y Cuarta (>25<40)
#08 Quinta (>10<25) y Sexta (<10km).
#98 No disponble.

	tags.update({'waterway':'x'})
	if attrs['CATEG_0301'] != '98' 
		tags.update({'waterway':'river'})
	else:	
		tags.update({'waterway':'stream'})

#Línea central del río o margen
	
	if attrs['COMPO_0301'] == '02'
		tags.update({'waterway':'riverbank'})
	  
	return tags

