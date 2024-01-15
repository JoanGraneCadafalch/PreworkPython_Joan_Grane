# EJERCICIOS CON VARIABLES Y OPERADORES
print('')
print('***VARIABLES Y OPERADORES***')
# 1. Ejercicio: Crea una variable llamada nombre y asígnale tu nombre como valor. Luego, imprime la variable.
print('1 Crea una variable llamada nombre y asígnale tu nombre como valor. Luego, imprime la variable.')
nombre = 'Joan'
print('      El nombre es: ',nombre)
print('')

# 2. Ejercicio: Crea dos variables, a y b , y asígnales los valores 5 y 10 respectivamente. Luego, imprime la suma de a y b.
print('2 Crea dos variables, a y b , y asígnales los valores 5 y 10 respectivamente. Luego, imprime la suma de a y b.')
a = 5
b = 10
print('      La suma es: ',a+b)
print('')

# 3. Ejercicio: Calcula el área de un triángulo con base 10 y altura 5.
print('3 Calcula el área de un triángulo con base 10 y altura 5.')
base = 10
altura = 5
area = base * altura / 2
print('      El area es: ',area)
print('')

# 4. Ejercicio: Calcula el resto de dividir 17 entre 3.
print('4 Calcula el resto de dividir 17 entre 3.')
division = 17 / 3
resto = division - int(division)
print('      El resto es: ',resto)
print('')

# EJERCICIOS CON CONDIONALES
print('')
print('***CONDICIONALES***')

# 1. Ejercicio: Dado un número, imprime si es positivo o negativo.
print('1 Dado un número, imprime si es positivo o negativo.')
num_pos_o_neg = -3
if num_pos_o_neg < 0:
  print(f'      El numero {num_pos_o_neg} es negativo')
else:
  print(f'      El numero {num_pos_o_neg} es positivo')
print('')

# 2. Ejercicio: Dado un número, imprime si es par o impar.
print('2 Dado un número, imprime si es par o impar.')
num_par_o_impar = 15
if num_par_o_impar % 2 == 0:
  print(f'      {num_par_o_impar} es par')
else:
  print(f'      {num_par_o_impar} es impar')
print('')

# 3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos
print('3 Dado tres números, encuentra y muestra el mayor de ellos.')
num_A = 4
num_B = 12
num_C = 5
if num_A > num_B and num_A > num_C:
  print(f'      De los números {num_A}, {num_B} y {num_C} el mayor es {num_A}')
elif num_B > num_C:
  print(f'      De los números {num_A}, {num_B} y {num_C} el mayor es {num_B}')
else:
  print(f'      De los números {num_A}, {num_B} y {num_C} el mayor es {num_C}')
print('')

# EJERCICIOS CON BUCLES
print('')
print('***BUCLES***')

# 1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for.
print('1 Imprime los números del 1 al 10 usando un bucle for.')
print('      ', end = "")
for Uno_a_Once in range(1,11):
  print(Uno_a_Once, end = " ")
print('')
print('')

# 2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while.
print('2 Imprime los números pares del 1 al 20 usando un bucle while.')
print('      ', end = "")
Uno_a_Veinte = 1
while  Uno_a_Veinte <= 20:
  if Uno_a_Veinte % 2 == 0:
    print(Uno_a_Veinte, end =" ")
  Uno_a_Veinte += 1
print('')
print('')

# 3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
print('3 Usa un bucle para calcular la suma de los números del 1 al 100.')
Uno_a_Cien = 1
Suma = 0
for Uno_a_Cien in range (1,101):
  Suma += Uno_a_Cien
print(f'      La suma es {Suma}')
print('')

# EJERCICIOS CON FUNCIONES
print('')
print('***FUNCIONES***')
# 1. Ejercicio: Define una función que tome dos números y retorne su suma.
print('1 Define una función que tome dos números y retorne su suma.')
num_D = 13
num_E =984
def sumar_numeros(a, b):
  return a + b
print(f'      La función suma {num_D} y {num_E} y nos devuelve {sumar_numeros(num_D,num_E)}')
print('')

# 2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
print('2 Defineuna función que tome un número y retorne su factorial.')
num_F = 12
def calcular_factorial (a):
  factorial = 1
  if a != 0 and a != 1:
    for i in range (1, a + 1):
      factorial *= i
  return factorial
print(f'      El factorial de {num_F} es {calcular_factorial(num_F)}')
print('')

# 3. Ejercicio: Define una función que tome un número y determine si es primo.
print('3 Define una función que tome un número y determine si es primo.')
num_G = 1447
def es_primo (a):
  if a <= 1: #para ser primo debe ser mayor que uno
    return False
  if a == 2: #2 es el único número par primo
    return True
  for n in range (2,a):
    if a % n == 0:
      return False
  return True
if es_primo(num_G) == True:
  print(f'      El número {num_G} es primo')
else:
  print(f'      El número {num_G} no es primo')
print('')

# 4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.
print('4 Define una función que reciba una lista de números y retorne la suma de ellos.')
num_H = 23
num_I = 12
num_J = 98
def suma_lista (a,b,c):
  return a + b + c
print(f'      Dados los números {num_H},{num_I},{num_J} la función nos da la suma {suma_lista(num_H,num_I,num_J)}')
print('')

# 5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa.
print('5 Define una función que reciba una cadena de texto y retorne la cadena en reversa.')
texto_a_girar = 'Yellow World'
def gira_texto (texto):
  return texto[::-1] #la he tenido que buscar, no tenia ni idea de como hacerlo.
print(f'      Damos el texto: {texto_a_girar} y nos retorna: {gira_texto(texto_a_girar)}')
print('')
