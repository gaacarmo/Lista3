soma = 0 
cont = 0
while cont < 10:
    nota =float(input("Digite uma nota: "))
    soma = soma + nota
    cont += 1
media = soma / cont
print(f"Sua média foi: {media}")
