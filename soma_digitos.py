n = input("Digite um número inteiro: ")
tamanho = len(n)
n = int(n)
soma = 0
while (tamanho >= 1):
    soma = soma + (n % 10)
    n = n // 10
    tamanho = tamanho - 1

print (soma)