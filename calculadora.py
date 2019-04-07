#!/usr/bin/env python
import sys
import os

diccionario = {'valor1':'',
'valor2':'',
'operacion':'',
'simbolo':'',
'resultado':''}
def suma(calc):
    try:
        res = calc['valor1']+calc['valor2']
    except Exception as exc:
        print(exc)
        res = None
    finally:
        return res

def resta(calc):
    try:
        res = calc['valor1']-calc['valor2']
    except Exception as exc:
        print(exc)
        res = None
    finally:
        return res

def multiplicacion(calc):
    try:
        res = calc['valor1']*calc['valor2']
    except Exception as exc:
        print(exc)
        res = None
    finally:
        return res

def division(calc):
    try:
        res = calc['valor1']/calc['valor2']
    except ZeroDivisionError:
        print("\n***\nNo se puede dividir para zero\n***")
        res = None
    except Exception as exc:
        print(exc)
        res = None
    finally:
        return res	
  
def exponente(calc):
    try:
        res = calc['valor1']**calc['valor2']
    except Exception as exc:
        print(exc)
        res = None
    finally:
        return res

while True:
    try:
        diccionario['valor1'] = float(input("*Ingrese el primer valor: "))
        break
    except ValueError:
        print("""
        Número invalido. 
        -Si ingresas números decimales debes colocar un punto(.) ya que no se admite comas(,)
        Intentalo de nuevo...
        """)

while True:
    try:
        diccionario['valor2'] = float(input("*Ingrese el segundo valor: "))
        break
    except ValueError:
        print("""
        Número invalido. 
        -Si ingresas números decimales debes colocar un punto(.) ya que no se admite comas(,)
        Intentalo de nuevo...
        """)

print("""
Escoger solo una opción
1.-Sumar
2.-Restar
3.-Multiplicar
4.-Dividir
5.-Exponencial
6.-Salir
""")

while True:
    try:
        diccionario['operacion'] = int(input("*Ingrese el número de la opción: "))
        if diccionario['operacion'] >= 1 and diccionario['operacion'] <= 6:
            break
        else:
            print("""
            Opción incorrecta
            Intentalo de nuevo...
            """)
    except ValueError:
        print("""
        Número invalido. 
        -Solo se admiten números enteros
        Intentalo de nuevo...
        """)
        

if diccionario['operacion'] == 1:
    diccionario['simbolo']='+'
    diccionario['resultado']=suma(diccionario)

elif diccionario['operacion'] == 2:
    diccionario['simbolo']='-'
    diccionario['resultado']=resta(diccionario)

elif diccionario['operacion'] == 3:
    diccionario['simbolo']='x'
    diccionario['resultado']=multiplicacion(diccionario)

elif diccionario['operacion'] == 4:
    diccionario['simbolo']='/'
    diccionario['resultado']=division(diccionario)

elif diccionario['operacion'] == 5:
    diccionario['simbolo']='^'
    diccionario['resultado']=exponente(diccionario)

else:
    sys.exit()

print ('\nLa respuesta de '+str(diccionario['valor1'])+diccionario['simbolo']+str(diccionario['valor2'])+' es = '+str(diccionario['resultado']))