from fileinput import close


a = 9
b = 4
respuesta = 0
for x in range(a):
    respuesta += b

print(respuesta)


nombre = "Jesús"
apellido = "Rdoríguez"

unir = nombre + " " + apellido

print(unir[::-1])


lista = [2, -800, -40000, 6, -9, -1000, 200]
menor = "init"
for x in lista:
    if menor == "init" or menor > x:
        menor = x
    elif menor < x:
        menor = menor
print(menor)


def calcularVolumen(r):
    return 4/3 * 3.14 * r ** 3

resultado = calcularVolumen(16)
print(resultado)


def esMayor(usuario):
    if usuario.edad > 17:
        return f"Es mayor de edad"
    else:
        return f"Es menor de edad"

class Usuario:

    def __init__(self, edad):
        self.edad = edad

usuario1 = Usuario(15)
usuario2 = Usuario(21)

resultado1 = esMayor(usuario1)
resultado2 = esMayor(usuario2)

print(resultado1)
print(resultado2)


def esPar(n):
    if n%2 == 0:
        return f"Es par"
    else:
        return f"Es impar"

print(esPar(5))
print(esPar(6))


palabra = "Yustaposición"
vocal = 0

for x in palabra:
    y = x.lower()
    if y == "a" or y == "e" or y == "i" or y == "o" or y == "u" or y == "ó":
        vocal += 1

print(vocal)


"""
Lista = []
print("Por favor ingrese núemros y para salir escriba basta")
while True:
    valor = input ("Ingrese un valor")
    if valor == "basta":
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print("Dato Invalido")
            exit()
resultado = 0
for x in lista:
    resultado += x

print(resultado)
"""


def agreagarNmbreyApellido(nombre, apellido):
    c = open("nombrecompleto.txt","a")
    c.write(nombre + " " + apellido + "\n")
    c.close()

agreagarNmbreyApellido("Diego", "Saavedra")
agreagarNmbreyApellido("Jesús", "Rodríguez")
agreagarNmbreyApellido("Juan", "Martínez")
agreagarNmbreyApellido("María", "Sarango")