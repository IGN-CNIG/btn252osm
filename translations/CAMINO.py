#!/usr/bin/python
# -*- coding: utf-8 -*-

# ogr2osm.py falla con el archivo Valencia/HUSO30/57058/BTN25_ETRS_BCN0623L_CAMINO_line.shp pues contiene un carácter de control o bit nulo

def filterTags(attrs):
        if not attrs: return

        tags={}
        tags.update({'highway':'track'})
        tags.update({'surface':'dirt'})
        tags.update({'tracktype':'grade2'})

# Nombre
        tags.update({'name':'x'})
        if attrs['ETIQUETA'] == "":
                del tags['name']
        else:
                tags ['name'] = attrs ['ETIQUETA']

# Situación SITUA_0623 (subterránea, superficial, elevada, vado)
        tags.update({'layer':'x'})
        if attrs['SITUA_0623'] == '01':
                tags.update({'layer':'-1'})
        elif attrs['SITUA_0623'] == '02':
                del tags['layer']
#               tags.update({'layer':'0'})
        elif attrs['SITUA_0623'] == '03':
                tags.update({'layer':'1'})
        elif attrs['SITUA_0623'] == '04':
                tags.update({'ford':'yes'})

        return tags
