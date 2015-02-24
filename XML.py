# -*- coding: utf-8 -*-

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
