print('')
# 1 Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar” según corresponda.
print('***BUCLES Y FUNCIONES NIVEL BÁSICO***')
print('1 Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar” según corresponda.')
num_par_o_impar = 143
if num_par_o_impar % 2 == 0:
  print(f'       {num_par_o_impar} es par')
else:
  print(f'       {num_par_o_impar} es impar')


# 2 Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado.
print('')
print('2 Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado.')
num_F = 8
def calcular_factorial (a):
  factorial = 1
  if a != 0 and a != 1:
    for i in range (1, a + 1):
      factorial *= i
  return factorial
print(f'       El factorial de {num_F} es {calcular_factorial(num_F)}')

# 3 Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado total de dígitos.
print('')
print('3 Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado total de dígitos.')
para_contar = 12345678
def vamos_a_contar (a):
  return len(str(a))
print(f'       El dígito {para_contar} tiene {vamos_a_contar(para_contar)} digitos')

# 4 Dada una lista de números, crea una función que devuelva el número máximo de la lista.
print('')
print('4 Dada una lista de números, crea una función que devuelva el número máximo de la lista.')
lista_de_numeros = [4, 53, 23, 3, 112, 78]
def encontrar_num_maximo (lista_numeros):
  maximo = lista_numeros[0]
  for n in lista_numeros:
    if n > maximo:
      maximo = n
  return maximo
print(f'       De la lista {lista_de_numeros} el máximo es {encontrar_num_maximo(lista_de_numeros)}')

# 5 Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.
print('')
print('5 Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.')
digitos_a_sumar = 1234
def suma_digitos (lista_digitos):
  suma = 0
  for n in str(lista_digitos): # Convertir el número a cadena para iterar sobre cada dígito
      suma += int(n)  # Convertir cada dígito a entero y sumarlo
  return suma
print(f'       El numero que le hemos dado es {digitos_a_sumar} y la suma de sus digitos nos da {suma_digitos(digitos_a_sumar)}')

# 6 Dados dos números, crea una función para encontrar el mínimo común múltiplo (MCM) de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM.
print('')
print('6 Dados dos números, crea una función para encontrar el mínimo común múltiplo (MCM) de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM.')
num_G = 6
num_H = 9 
def MCM (MCM_a,MCM_b):
  def mcd (mcd_a,mcd_b):
    while mcd_b != 0:
      mcd_a, mcd_b = mcd_b, mcd_a % mcd_b
    return mcd_a
  return abs (MCM_a * MCM_b) / mcd (MCM_a,MCM_b)
print(f'       De los números {num_G} y {num_H} el Máximo Común Múltiplo (MCM) es: {MCM(num_G,num_H)}')

# 7 Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo.
print('')
print('7 Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo.')
base = 10
altura = 5
def area_triangulo(b,h):
  area = b * h / 2
  return area
print(f'       El area de un triangulo de base {base} y altura {altura} es {area_triangulo(base,altura)}')

# 8 Crea una función que, dado un número, verifique si un número es positivo, negativo o cero.
print('')
print('8 Crea una función que, dado un número, verifique si un número es positivo, negativo o cero.')
num_I = -23
def pos_neg_0 (valor):
  if valor == 0:
    return "Cero"
  elif valor > 0:
    return "Positivo"
  else:
    return "Negativo"
print(f'       El número {num_I} es {pos_neg_0(num_I)}')

# 9 Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.
print('')
print('9 Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.')
palabra = "Historia"
def num_letras (text):
  return len(text)
print(f'       La palabra {palabra} tiene {num_letras(palabra)} letras.')

# 10 Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto.
print('')
print('10 Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto.')
lista_de_numeros_abs = (-3, 12, -5, 0, -12)
def convierte_a_absolutos (lista_nums):
  lista_nums_abs = []
  for numero in lista_nums:
   lista_nums_abs.append(abs(numero))
  return lista_nums_abs
print(f'       De la lista original {lista_de_numeros_abs} obtenemos la lista en absoluta {convierte_a_absolutos(lista_de_numeros_abs)}')

# 11 Crea una función que, dado un número, verifique si un número es primo.
print('')
print('11 Crea una función que, dado un número, verifique si un número es primo.')
num_J = 1447
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
  print(f'       El número {num_J} es primo')
else:
  print(f'       El número {num_J} no es primo')

# 12 Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números.
print('')
print('12 Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números.')
num_K = 30
num_L = 75
def mcd (mcd_a,mcd_b):
    while mcd_b != 0:
      mcd_a, mcd_b = mcd_b, mcd_a % mcd_b
    return mcd_a
print(f'       El mínimo común divisor de los números {num_K} y {num_L} es {mcd(num_K,num_L)}')

print('')

