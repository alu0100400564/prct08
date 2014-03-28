#!/usr/bin/python

import modulo
import math
import sys

pi = 3.1415926535897931159979634685441852
def error(num_int, num_test, umbral):
  errores=0
  for i in range(num_test):
    s=modulo.aproximacionpi(num_int)
    valor=abs(s-pi)
    if valor>=umbral:
      errores+=1
  p_error=(errores/num_test)*100
  return p_error 
if __name__=="__main__":
  if (len(sys.argv)==4):
    num_int = int(sys.argv[1])
    num_test = int(sys.argv[2])
    umbral = float(sys.argv[3])
  else:
    num_int = int(raw_input('Introduzca el numero de intervalos ')) 
    num_test = int(raw_input('Introduzca el numero de tests '))
    umbral = float(raw_input('Introduzca el valor del umbral '))
  porcentaje=error(num_int, num_test, umbral)
  print porcentaje
