from lxml import etree
xml=etree.parse("ayudas_0.xml")
ayudas=xml.getroot()

print ayudas[9].text
#for i in xrange(len(ayudas)):
#	print ayudas[i][2].text

#for ayuda in ayudas:
#	print ayuda.findtext("titulo")
#	presentacion=ayuda.find("plazopresentacion")
#	plazopresentacion_item=ayuda.find("plazopresentacion_item")
#	print plazopresentacion_item.findtext("incial")
#	print plazopresentacion_item.findtext("final")
#	print ayuda.findtext("descripcion")
#	print "---------------------------------------"
