#!/usr/bin/python

import modulo
import ej8
import math
import sys

if __name__=="__main__":
  print ('Introduzca el nombre para el fichero')
  nombre = raw_input()
  if (len(sys.argv)==8):
    num_int = int(sys.argv[1])
    num_test = int(sys.argv[2])
    umbral = []
    for i in range (3,8):
      umbral.append(float(sys.argv[i]))
    
  else:
    num_int = int(raw_input('Introduzca el numero de intervalos ')) 
    num_test = int(raw_input('Introduzca el numero de tests '))
    print ('Introduzca los 5 valores del umbral ')
    umbral = []
    for i in range (5):
      print 'Introduzca el umbral',i+1
      umbral.append(float(raw_input()))   
  fichero = open (nombre, 'w')
  fichero.write
  for i in range (5):
    porcentaje = ej8.error(num_int, num_test, umbral)
    fichero.write (porcentaje)
  fichero.close ()  
      
      