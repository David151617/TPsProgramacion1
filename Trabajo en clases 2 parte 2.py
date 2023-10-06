numeros = []
pares = 0
impares = 0
while True:
    try:
        entrada = input("Ingrese un número entero (ingrese 0 para terminar)")
        numero = int(entrada)
        if numero == 0:
            break
        numeros.append(numero)
    except ValueError:
        print("Entrada incorrecta. Ingrese un número válido")

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        pares += 1
    if numeros[i] %2 != 0:
        impares += 1

print("La cantidad total de numeros pares son: ",pares)
print("La cantidad total de números impares son: ", impares)    