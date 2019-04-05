#!/usr/bin/env python
import sys
import os

def suma(x,y):
	res = x+y
	print (res)

def resta(x,y):
	res = x-y
	print (res)

def multiplicacion(x,y):
	res = x*y
	print (res)

def division(x,y):
	res = x/y
	print (res)

x = float(input("ingrese un valor1: "))
y = float(input("ingrese un valor2: "))
op = input("escoja operacion: ")
name = input("Enter a name: ")
print(name)
if op == 'suma':
	suma(x,y)
elif op == 'resta':
	resta(x,y)
elif op == 'multi':
	multiplicacion(x,y)
elif op == 'division':
	division(x,y)
else:
	print ('operacion no encontrada')
