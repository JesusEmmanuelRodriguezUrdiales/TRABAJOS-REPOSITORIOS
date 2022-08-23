dato = 2 #input("Por favor ingrese algo: ")

print(dato)
    
lista = ["Hola","Mundo"]
    
if lista.count(dato) > 0:
    print("Esta información existe:", dato)
else:
    print("Esta información no existe", dato)



primerNumero = 4 #input("Ingrese el primer número: ")
segundoNumero = 5 #input("Ingrese el segundo número: ")

print(primerNumero + segundoNumero)



primerNumero = 5 #input("Ingrese el primer número: ")
segundoNumero = 6 #input("Ingrese el segundo número: ")

primero = int(primerNumero)
segundo = int(segundoNumero)

print(primero + segundo)



primerNumero = 5 #input("Ingrese el primer número: ")
segundoNumero = 6 #input("Ingrese el segundo número: ")

primero = int(primerNumero)
segundo = int(segundoNumero)

print(primero + segundo)



primerNumero = 9 #input("Ingrese el primer número: ")

try:
    primero = int(primerNumero)
except:
    primero = "Cadena"

if primero == "Cadena":
    print("El valor ingresado no es un entero")
    exit()

segundoNumero = 8 #input("Ingrese el segundo número: ")

try:
    segundo = int(segundoNumero)
except:
    segundo = "Cadena"

if segundo == "Cadena":
    print("El valor ingresado no es un entero")
    exit()

simbolo = "+" #input("Ingrese la operacion: ")

if simbolo == "+":
    print("Suma: ", primero + segundo)
elif simbolo == "-":
    print("Resta: ", primero - segundo)
elif simbolo == "*":
    print("Multiplicacion: ", primero * segundo)
elif simbolo == "/":
    print("Division: ", primero / segundo)
else:
    print("El simbolo ingresado no es valido")