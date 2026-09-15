primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
numero = 67
inicio = 0
fim = len(primos)

while inicio <= fim:
    meio = (inicio + fim) // 2
    if primos[meio] < numero:
        inicio = meio + 1
    else:
        fim = meio

print("Quantidade de numeros menores que 67:", inicio)