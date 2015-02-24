# -*- coding: utf-8 -*-
import os
from lxml import etree
xml=etree.parse("ayudas_0.xml")
ayudas=xml.getroot()

for ayuda in ayudas:
	print ayuda.findtext("titulo")
	presentacion=ayuda.find("plazopresentacion")
	plazopresentacion_item=presentacion.find("plazopresentacion_item")
	print plazopresentacion_item.findtext("incial")
	print plazopresentacion_item.findtext("final")
	print ayuda.findtext("descripcion")
	print "---------------------------------------"

print ""
raw_input("Pulsa intro para iniciar ejercicio 2")
os.system('clear')

for ayuda in ayudas:
	print ayuda.findtext("titulo")
	print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - "
	documentacion=ayuda.find("documentacion")
	
	for documentacion_item in documentacion:
		print documentacion_item.findtext("titulo")
		print ""
				
	print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
	
print ""
raw_input("Pulsa intro para iniciar ejercicio 3")
os.system('clear')


abierto=0
cerrado=0
for ayuda in ayudas:
	if ayuda.findtext("estado")=="Cerrado":
		cerrado=cerrado+1
	else:
		abierto=abierto+1

print "Hay ",abierto," ayudas abiertas"
print "Hay ",cerrado," ayudas cerradas"

raw_input("Pulsa intro para iniciar ejercicio 4")
os.system('clear')

titulo=raw_input("Introduce el titulo de la beca que desea consultar: ")

for ayuda in ayudas:
	if str(ayuda.findtext("titulo"))==titulo:
		print ayuda.findtext("titulo")
		presentacion=ayuda.find("plazopresentacion")
		plazopresentacion_item=presentacion.find("plazopresentacion_item")
		print plazopresentacion_item.findtext("incial")
		print plazopresentacion_item.findtext("final")
		print ayuda.findtext("descripcion")
