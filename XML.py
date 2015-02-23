from lxml import etree
ayudas=etree.parse("ayudas_0.xml")
raiz=ayudas.getroot()

ayudas=ayudas.findall("ayuda")

for ayuda in ayudas:
	print ayuda.findtext("titulo")
	presentacion=ayuda.find("plazopresentacion")
	plazopresentacion_item=ayuda.find("plazopresentacion_item")
#	print plazopresentacion_item.findtext("incial")
#	print plazopresentacion_item.findtext("final")
	print ayuda.findtext("descripcion")
	print "---------------------------------------"
