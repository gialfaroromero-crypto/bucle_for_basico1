# bucle_for_basico1.py


print("Ejercicio 1: Básico")
for i in range(0, 101):  # range va hasta 100 inclusive
    print(i)


print("\nEjercicio 2: Múltiples de 2")
for i in range(2, 501, 2):  # empieza en 2, avanza de 2 en 2
    print(i)



print("\nEjercicio 3: Contando Vanilla Ice")
for i in range(1, 101):
    if i % 10 == 0:  # divisible por 10
        print("baby")
    elif i % 5 == 0:  # divisible por 5
        print("ice ice")
    else:
        print(i)



print("\nEjercicio 4: Número gigante")
suma = 0

for i in range(0, 500001, 2):  # solo pares
    suma += i  # acumulamos

print("Suma total:", suma)



print("\nEjercicio 5: Regresando de 3 en 3")
for i in range(2024, 0, -3):  # cuenta regresiva
    print(i)



print("\nEjercicio 6: Contador dinámico")

numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:  # verifica si es múltiplo
        print(i)