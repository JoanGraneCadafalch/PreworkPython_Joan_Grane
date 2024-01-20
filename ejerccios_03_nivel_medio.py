# 1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci.
print('')
print('BUCLES Y FUNCIONES NIVEL MEDIO')
print('1 Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci.')
num_A = 12
def imprime_fibonacci (num):
  a, b = 1, 1
  num_fibonacci = [1]
  for iteraciones in range(num-1):
      num_fibonacci.append(b)
      a, b = b, a+b
  return num_fibonacci
print(f'     Los {num_A} numeros de la serie de Fibonacci son {imprime_fibonacci(num_A)}')

# 2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores.
print('')
print('2 Define una función que tome un número y retorne una lista de sus divisores.')
num_B = 144
def return_divisores (num):
  lista_divisores = []
  for i in range(1,num):
    if num % i == 0:
      lista_divisores.append(i)
  return lista_divisores
print(f'     Los divisores del número {num_B} son {return_divisores(num_B)}')

# 3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.
print('')
print('3 Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.')
lista_elementos = [3, 4, 1, 3, 12, 8, 3, 1]
def elem_unicos (lista):
  lista_unica = list(set(lista))
  return lista_unica
print(f'     Los elementos únicos de la lista {lista_elementos} son {elem_unicos(lista_elementos)}')

# 4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos.
print('')
print('4 Define una función que tome un número y retorne la suma de sus dígitos.')
digitos_a_sumar = 557382
def suma_digitos (lista_digitos):
  suma = 0
  for n in str(lista_digitos): 
      suma += int(n) 
  return suma
print(f'     El numero que le hemos dado es {digitos_a_sumar} y la suma de sus digitos nos da {suma_digitos(digitos_a_sumar)}')

# 5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena.
print('')
print('5 Define una función que tome una cadena y cuente el número de vocales en la cadena.')
palabra = 'Otorrinolaringologo'
def cuenta_vocales (palabra):
  num_vocales = 0
  vocales = 'aeiouAEIOU'
  for caracter in palabra:
    if caracter in vocales:
      num_vocales += 1
  return num_vocales
print(f'     El número de vocales de la palabra {palabra} es {cuenta_vocales(palabra)}')

# 6. Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.
print('')
print('6 Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.')
num_C = 4
lista_elementos = [3, 4, 2, 4, 5, 3, 4, 6, 7, 1]
def n_elementos (n,lista):
  return lista[:n]
print(f'     Los primeros {num_C} de la {lista_elementos} son {n_elementos(num_C,lista_elementos)}')

# 7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.
print('')
print('7 Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.')
frase = 'En un Lugar muy Especial'
def num_may_min (texto):
  contador_may = 0
  contador_min = 0
  for caracter in texto:
    if caracter.isupper():
      contador_may += 1
    elif caracter.islower():
      contador_min += 1
  return contador_may, contador_min
print(f'     La frase "{frase}" tiene {num_may_min(frase)} mayúsculas y minúsculas respectivamente')

# 8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
print('')
print('8 Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario.')
num_D = 6
def es_perfecto(num):
  suma_divisores = 0
  for n in range(1,num):
    if num % n == 0:
      suma_divisores += n
  if num == suma_divisores:
    return True
  else:
    return False
print(f'     El número {num_D} es perfecto? {es_perfecto(num_D)}.')

# 9. Ejercicio: Define una función que reciba un número y retorne su representación en binario.
print('')
print('9 Define una función que reciba un número y retorne su representación en binario.')
num_E = 16
def num_en_binario (num_decimal):
  num_binario = bin(num_decimal)[2:]
  return num_binario
print(f'     El número {num_E} en binario es {num_en_binario(num_E)}')

# 10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).
print('')
print('10 Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).')
conjunto1 = [2, 4, 6, 8, 10, 12, 14, 16]
conjunto2 = [1, 2, 3, 4, 5, 6, 7, 8]
def busca_interseccion (listA,listB):
  conjuntoA = set(listA) #convierte la lista en conjunto
  conjuntoB = set(listB)
  interseccion = conjuntoA.intersection(conjuntoB) #busca la intersección
  return list(interseccion) #convierte el conjunto en lista
print(f'     Los intersección de las listas [{conjunto1}] y [{conjunto2}] es [{busca_interseccion(conjunto1,conjunto2)}]')

# 11. Ejercicio: Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
print('')
print('11 Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).')
cadena = 'ala'
def es_palindrome (textoA):
  textoB = textoA[::-1]
  if textoA == textoB:
    return True
  else:
    return False
print(f'     La cadena "{cadena}" es palíndrome? {es_palindrome(cadena)}')

# 12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.
print('')
print('12 Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.')
print(f'     Lista del 1 al 50 es: ',end = "")
for n in range (1,51):
  if n % 15 == 0:
    print('FizzBuzz ',end ="")
  elif n % 3 == 0:
    print('Fizz ',end ="")
  elif n % 5 == 0:
    print('Buzz ',end ="")
  else:
    print(n,' ',end ="")
print('')

# 13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente.
print('')
print('13 Define una función que tome una lista y retorne la lista ordenada en orden ascendente.')
lista_caos = [3, 5, 1, 6, 89, 31, 101]
def ordena_la_lista (lista):
  return sorted (lista)
print(f'     La lista {lista_caos} ordenada es: {ordena_la_lista(lista_caos)}')

# 14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.
print('')
print('14 Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.')
lista_palabras = ['hola', 'ola', 'arriba', 'corred', 'parad', 'esperadme']
num_letras = 5
def palabras_largas(lista_completa,num):
  lista_reducida = []
  for palabra in lista_completa:
    if len(palabra) > num:
      lista_reducida.append (palabra)
  return lista_reducida
print(f'     De la lista [{lista_palabras}] las palabras más largas que {num_letras} són: {palabras_largas(lista_palabras,num_letras)}')

# 15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci.
print('')
print('15 Define una función que tome un número y calcule su serie de Fibonacci.')
num_F = 10
def num_fibonacci (num):
  serie = [0,1]
  if num <= 0:
    return []
  elif num == 1:
    return [0]
  elif num == 2:
    return serie
  for i in range (2,num):
    siguiente_numero = serie[i - 1]+ serie [i -2]
    serie.append(siguiente_numero)
  return serie
print(f'     La serie de Fibonacci de {num_F} es: {num_fibonacci(num_F)}')

# 16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista.
print('')
print('16 Define una función que tome una lista de números y retorne el número más grande de la lista.')
lista_numeros = [2, 3, 9, 5, 7]
def numero_mas_grande(lista):
  num = max(lista)
  return num
print(f'     El número más grande de la lista [{lista_numeros}] es: {numero_mas_grande(lista_numeros)}')

# 17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
print('')
print('17 Define una función que reciba un número y retorne la suma de sus dígitos al cubo.')
num_G = 1234
def num_al_cubo (num):
  num_cubo = 0
  cadena_num = str(num) #convierte el número a una cadena para iterar sobre cada dígito
  for digito in cadena_num:
    num_cubo += int(digito)
  num_cubo = num_cubo**3
  return num_cubo
print(f'     La suma al cubo del número {num_G} es: {num_al_cubo(num_G)}')

# 18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
print('')
print('18 Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.')
lista_numeros_B = [2, 3, 9, 5, 7]
def segundo_mas_grande(lista):
  lista_numeros_unicos = list(set(lista))
  if len(lista_numeros_unicos) < 2:
    return None
  else:
    lista_numeros_unicos.sort(reverse=True)
    print(lista_numeros_unicos)
    return lista_numeros_unicos[1]
print(f'     El segundo número más grande de la lista [{lista_numeros_B}] es: {segundo_mas_grande(lista_numeros_B)}')
print(f'     ')

# 19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.
print('')
print('19 Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.')
lista_comparar_A = [1, 3, 5, 7]
lista_comparar_B = [4, 5, 6]
def compara_listas (lista1,lista2):
  conjunto1 = set(lista1)
  conjunto2 = set(lista2)
  return not conjunto1.isdisjoint(conjunto2)
print(f'¿Las listas {lista_comparar_A} y {lista_comparar_B} tienen algún número en común? {compara_listas(lista_comparar_A,lista_comparar_B)}')
print(f'     ')

# 20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.
print('')
print('20 Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.')
lista_a_girar = [1, 2, 3, 4, 5]
def gira_lista (lista_original):
  lista_original.reverse()
  return lista_original
print(f'La lista {lista_a_girar} girada es {gira_lista(lista_a_girar)}')
print(f'     ')

# 21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
print('')
print('21 Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.')
cadena_A = "Hoy tenemos 234 casos distintos"
def cuenta_digitos_letras(cadena):
  contador_digitos = 0
  contador_letras = 0
  for caracter in cadena:
    if caracter.isdigit():
      contador_digitos += 1
    elif caracter.isalpha():
      contador_letras += 1  
  return contador_digitos, contador_letras
print(f'La cadena "{cadena_A}" tiene tantos dígitos y letras como: {cuenta_digitos_letras(cadena_A)}')
print(f'     ')

# 22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números.
print('')
print('22 Define una función que reciba una lista de números y retorne la suma acumulada de los números.')
lista_a_sumar = [1, 3, 5, 7, 9]
def suma_listas (lista):
  sumatorio = sum(lista)
  return sumatorio
print(f'La suma acumulada de la lista {lista_a_sumar} es {suma_listas(lista_a_sumar)}')
print(f'     ')

# 23. Ejercicio: Define una función que encuentre el elemento más común en una lista.
print('')
print('23 Define una función que encuentre el elemento más común en una lista.')
lista_elementos_B = [1, 3, 4, 1, "a", "b", "c", "d", 2, 3, "a", "a"]
def busca_el_mas_comun (lista):
  conteo = {}
  for elemento in lista:
    if elemento in conteo:
      conteo[elemento] += 1
    else:
      conteo[elemento] = 1
  max_apariciones = 0
  elemento_comun = None
  for elemento, cantidad in conteo.items():
    if cantidad > max_apariciones:
      max_apariciones = cantidad
      elemento_comun = elemento
  return elemento_comun
print(f'El elemento más común de la lista {lista_elementos_B} es {busca_el_mas_comun(lista_elementos_B)}')
print(f'     ')

# 24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.
print('')
print('24 Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.')
num_H = 8
def tabla_multiplicar (numero):
  tabla = {}
  for i in range (1,11):
    tabla[i] = numero * i
  return tabla
print(f'La tabla de multiplicar de {num_H} es {tabla_multiplicar(num_H)}')
print(f'     ')

# 25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.
print('')
print('25 Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.')
cadena_B = ["a", "b", "a", "b", "c", "c","c", 4, 5, 6, 7, 6, 5, 4, 5, 6, 5, 4]
def num_apariciones (cadena):
  diccionario = {}
  for caracter in cadena:
    if caracter in diccionario:
      diccionario[caracter] += 1
    else:
      diccionario[caracter] = 1
  return diccionario
print(f'La cadena {cadena_B} tiene tantas apariciones como {num_apariciones(cadena_B)}')
print(f'     ')

# 26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
print('')
print('26 Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.')
lista_A = [1, 2, 3, 4, 5]
lista_B = [2, 4, 6]
def no_comunes(listA,listB):
  list_no_comons = []
  conjunto1 = set(listA)
  conjunto2 = set(listB)
  list_no_comons = conjunto1.symmetric_difference(conjunto2)
  return list_no_comons
print(f'De las listas {lista_A} y {lista_B} los elementos no comunes son {no_comunes(lista_A,lista_B)}')
print(f'     ')

# 27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados.
print('')
print('27 Define una función que tome una lista y retorne la lista sin duplicados.')
lista_C = [1, 2, 3, 1, 2, 3, 1, 2, 3]
def no_duplicados(lista):
  lista_sin_duplicados = list(set(lista))
  return lista_sin_duplicados
print(f'De la lista {lista_C}, la lista sin duplicados es{no_duplicados(lista_C)}')
print(f'     ')

# 28. Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.
print('')
print('28 Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.')
num_I = 4
def suma_cuadrados_pares(num):
  suma = 0
  for i in range(1,num+1):
    if i % 2 == 0:
      suma += i**2
  return suma
print(f'La suma de los cuadrados de los números pares o iguales a {num_I} es {suma_cuadrados_pares(num_I)}')
print(f'     ')

# 29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista.
print('')
print('29 Define una función que reciba una lista de números y retorne el promedio de los números en la lista.')
lista_D = [1, 3, 5, 7, 9, 11]
def promedio_lista(lista):
  promedio = sum(lista) / len(lista)
  return promedio
print(f'El promedio de la lista {lista_D} es {promedio_lista(lista_D)}')
print(f'     ')

# 30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
print('')
print('30 Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.')
lista_E = ["hola","adios","hellow","good bye"]
def cadena_larga(lista):
  mas_larga = ""
  for cadena in lista:
    if len(cadena) > len(mas_larga):
      mas_larga = cadena
  return mas_larga
print(f'La cadena más larga de la lista {lista_E} es "{cadena_larga(lista_E)}"')
print(f'     ')

# 31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.
print('')
print('31 Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.')
num_J = 12
def es_primo (a):
  if a <= 1: #para ser primo debe ser mayor que uno
    return False
  if a == 2: #2 es el único número par primo
    return True
  for n in range (2,a):
    if a % n == 0:
      return False
  return True
def lista_primos(numero):
  primos = []
  num = 2
  while len(primos) < numero:
    if es_primo(num):
      primos.append(num)
    num +=1
  return primos
print(f'Los {num_J} primeros números primos son {lista_primos(num_J)}')
print(f'     ')

# 32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.
print('')
print('32 Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.')
cadena_B = "Vamos a girar las palabras"
def gira_palabras (cadena):
  palabras = cadena.split()
  palabras_giradas = palabras[::-1]
  cadena_girada = ' '.join(palabras_giradas)
  return cadena_girada
print(f'La cadena "{cadena_B}" girada es "{gira_palabras(cadena_B)}"')
print(f'     ')

# 33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.
print('')
print('33 Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.')
lista_F = [("Elena", 23),("Pedro", 21),("Beatriz", 29),("Jorge", 26)]
def ordena_lista_tuplas(lista):
  n = len(lista)
  for i in range (n):
    for j in range (0,n-i-1):
      if lista[j][-1] > lista[i][-1]:
        lista[j], lista[j+1] = lista [j+1], lista[j]
  return lista
print(f'Una vez ordenada la lista {lista_F} obtenemos {ordena_lista_tuplas(lista_F)}')
print(f'     ')

# 34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.
print('')
print('34 Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.')
cadena_C ="murciElago"
def num_vocales(cadena):
  vocales = "aeiouAEIOU"
  num = 0
  for caracter in cadena:
    if caracter in vocales:
      num += 1
  return num
print(f'El número de vocales de la cadena "{cadena_C}" es {num_vocales(cadena_C)}')
print(f'     ')

# 35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False.
print('')
print('35 Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False.')
num_K = 67
def es_primo (a):
  if a <= 1:
    return False
  if a == 2:
    return True
  for n in range (2,a):
    if a % n == 0:
      return False
  return True
print(f'¿El número {num_K} es primo? {es_primo(num_K)}')
print(f'     ')