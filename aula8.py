# passagem de argumentos.
import sys

argumentos = sys.argv  # arq1 metodo // arg2 -> num1 // arg3 -> num2

def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

if argumentos[1] == 'soma':
    resp = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == 'sub':
    resp = sub(float(argumentos[2]), float(argumentos[3]))
else:
    resp = '** COMANDO INVALIDO **'

print(resp)
# print(argumentos)
