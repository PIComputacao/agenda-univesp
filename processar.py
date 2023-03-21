#!/python25/python
# -*- coding: UTF-8 -*-
 
# Código para processar.py
 
import cgi
 
print "Content-Type: text/html\n"
 
formulario = cgi.FieldStorage()
nome = formulario.getvalue("nome")
 
print "Olá, seu nome é: " + nome