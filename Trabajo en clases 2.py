def cifra_cesar(texto, corrimiento):
    texto_encriptado = ""
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Alfabeto en mayúsculas

    for caracter in texto:
        if caracter.isalpha():  # Verificar si el caracter es una letra
            mayuscula = caracter.isupper()
            caracter = caracter.upper()
            indice = alfabeto.index(caracter)
            nuevo_indice = (indice + corrimiento) % 26
            nuevo_caracter = alfabeto[nuevo_indice]
            if not mayuscula:
                nuevo_caracter = nuevo_caracter.lower()
            texto_encriptado += nuevo_caracter
        else:
            texto_encriptado += caracter

    return texto_encriptado

# Solicitar al usuario el corrimiento
corrimiento = int(input("Ingrese la cantidad de lugares a correr las letras: "))

# Solicitar los mensajes a encriptar
mensajes = []
for i in range(5):
    mensaje = input(f"Ingrese el mensaje {i+1}: ")
    mensajes.append(mensaje)

# Encriptar los mensajes con el mismo corrimiento
for mensaje in mensajes:
    mensaje_encriptado = cifra_cesar(mensaje, corrimiento)
    print("Mensaje encriptado:", mensaje_encriptado)