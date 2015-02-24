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
raw_input("Pulsa intro para iniciar ejercicio2")
os.system('clear')

for ayuda in ayudas:
	print ayuda.findtext("titulo")
	print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - "
	documentacion=ayuda.find("documentacion")
	
	for documentacion_item in documentacion:
		print documentacion_item.findtext("titulo")
		print ""
				
	print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
