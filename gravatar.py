# -*- coding: utf-8 -*-
from hashlib import md5

alum = open('alumnos.csv','r') 
grav = open('gravatar.html','w')
grav.writelines('''<!DOCTYPE html PUBLIC "-// W3C//DTD XHTML 1.0 Strict//EN" "ht\
tp://www.w3.org/TR/xhtml1/DTD/xhtml1-strict .dtd">
<html xmlns ="http://www.w3.org/1999/xhtml" xml:lang="es">
	<head>
		<title>Avatares del Gonzalo Nazareno</title>
	</head>''')

for linea in alum:
	grav.writelines('''<body>
		<p><img src='http://gravatar.com/avatar/''')
	lista = linea.split(",")
	nombre = lista[0]
	correo = lista[1]
	hashh = md5(correo[1:][:-1]).hexdigest()
	grav.writelines(hashh)
	grav.writelines("' alt='avatar' height='100' width='100'/>")
	grav.writelines(nombre)
grav.writelines('''</p>
	</body>
</html>''')

