#Inicialize uma lista de 20 números inteiros. Armazene os números pares em uma lista PAR e os números ímpares em uma lista IMPAR. Imprima as listas PAR e IMPAR. 

numeros = []
pares = []
impares = []

for i in range(1,21):
    numero = int(input(f"digite o numero {i}:  "))
    numeros.append(numero)

for item in numeros:
    if item % 2 == 0:
        pares.append(item)
    elif item % 2 != 0:
        impares.append(item)

print("os numeros pares são:")
print(pares)
print("os numeros impares são:")
print(impares)