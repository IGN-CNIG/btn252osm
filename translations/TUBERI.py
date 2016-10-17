#!/usr/bin/python
# -*- coding: utf-8 -*-

def filterTags(attrs):
	if not attrs: return

	tags={}
	tags.update({'man_made':'pipeline'})
	tags.update({'substance':'water'})

#Situación.01 Subterraneo. 02 Superficial. 03 Elevado.
	tags.update({'tunnel':'x'})
	tags.update({'bridge':'x'})
	if attrs['SITUA_0307'] == '01':
		tags.update({'tunnel':'yes'})
	else:
		del tags['tunnel']
	if attrs['SITUA_0307'] == '03':
		tags.update({'bridge':'aqueduct'})
	else:
		del tags['bridge']
		
	return tags

