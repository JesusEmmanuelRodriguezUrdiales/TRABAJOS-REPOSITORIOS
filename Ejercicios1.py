from glob import escape
from re import I


dato = 2 #imput("Por favor ingrese algo: ")

print(dato)

lista = ["Hola","Mundo"]

if lista.count(dato) > 0:
    print("Esta información existe:", dato)
else:
    print("Esta inofmración existe", dato)


primerNúmero = 4 #imput("Ingrese el primer número: ")
segundoNúmero = 5 #imput("Ingrese el segundo número: ")

print(primerNúmero + segundoNúmero)


primerNúmero = 5 #imput("Ingrese el primer número: ")
segundoNúmero = 6 #imput("Ingrese el segundo número: ")

primero = int(primerNúmero)
segundo = int(segundoNúmero)

print(primerNúmero + segundoNúmero)


primerNúmero = 6 #imput("Ingrese el primer número: ")

try:
    primero = int (primerNúmero)
except:
    primero = "Cadena"

segundoNúmero = 8 #imput("Ingrese el segundo número: ")

try:
    segundo = int(segundoNúmero)
except:
    segundo = "Cadena"

if primero == "Cadena" or segundo == "Cadena":
    print ("Ingreso mal un dato, pruebe por favor una vez más ingresando números")
else:
    print(primero + segundo)


primerNúmero = 9 #imput("Ingrese el primer número: ")

try:
    primero = int(primerNúmero)
except:
    primero = "Cadena"

segundoNúmero = 6 #imput("Ingrese el segundo núemro: ")

try:
    segundo = int(segundoNúmero)
except:
    segundo = "Cadena"

if primero == "Cadena" or segundo == "Cadena":
    print("Ingreso mal un dato, pruebe por favor una vez más ingersando números")
else:
    print(primero + segundo)

primerNúmero = 9 #input("Ingrese el primer número: ")

try:
    primero = int(primerNúmero)
except:
    primero = "Cadena"

if primero == "Cadena":
    print("El valor ingresado no es un entero")
    exit()

segundoNúmero = 8 #input("Ingrese el segundo número")

try:
    segundo = int(segundoNúmero)
except:
    segundo = "Cadena"

if segundo == "Cadena":
    print("El valor ingresado no es un entero")
    exit()

simbolo = "+" #input("Ingrese la operación: ")

if simbolo == "+":
    print("Suma: ", primero + segundo)
elif simbolo == "-":
    print("Resta: ", primero - segundo)
elif simbolo == "*":
    print("Multiplicaión: ", primero * segundo)
elif simbolo == "/":
    print("División: ", primero / segundo)
else:
    print("El símbolo ingresado no es valido")
    