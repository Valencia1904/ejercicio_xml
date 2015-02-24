# -*- coding: utf-8 -*-
import os
from lxml import etree
xml=etree.parse("ayudas_0.xml")
ayudas=xml.getroot()

for ayuda in ayudas:
	print "Titulo: ",ayuda.findtext("titulo")
	presentacion=ayuda.find("plazopresentacion")
	plazopresentacion_item=presentacion.find("plazopresentacion_item")
	print "Fecha inicial: ",plazopresentacion_item.findtext("incial")
	print "Fecha final: ",plazopresentacion_item.findtext("final")
	print "Descripcion:"
	print ayuda.findtext("descripcion")
	print "---------------------------------------"

print ""
raw_input("Pulsa intro para iniciar ejercicio 2")
os.system('clear')

for ayuda in ayudas:
	print ayuda.findtext("titulo")
	print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - "
	documentacion=ayuda.find("documentacion")
	print "Documentos necesarios:"
	
	for documentacion_item in documentacion:
		print documentacion_item.findtext("titulo")
		print ""
				
	print"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
	
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
	titulo2=str(ayuda.findtext("titulo").encode('utf-8'))
	if titulo2==titulo:
		print "Titulo: ",ayuda.findtext("titulo")
		presentacion=ayuda.find("plazopresentacion")
		plazopresentacion_item=presentacion.find("plazopresentacion_item")
		print "Fecha inicio: ",plazopresentacion_item.findtext("incial")
		print "Fecha final: ",plazopresentacion_item.findtext("final")
		print "Descripcion: "
		print ayuda.findtext("descripcion")
		
raw_input("Pulsa intro para iniciar ejercicio 5")
os.system('clear')

fecha = raw_input("Introduce una fecha (YYYY-MM-DD): ")
fecha =fecha.split('-')

for ayuda in ayudas:
	presentacion=ayuda.find("plazopresentacion")
	plazopresentacion_item=presentacion.find("plazopresentacion_item")
	fecha2=plazopresentacion_item.findtext("incial").split("T")
	fecha2=fecha2[0].split("-")
	if fecha[0] <= fecha2[0]:
		if fecha[1] <= fecha2[1]:
			if fecha[2] <= fecha2[2]:
				print "Titulo: ",ayuda.findtext("titulo")
				print "Fecha inicio: ",plazopresentacion_item.findtext("incial")
				print "Fecha final: ",plazopresentacion_item.findtext("final")
				print ""
				print "Descripcion:"
				print ayuda.findtext("descripcion")
				print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"


