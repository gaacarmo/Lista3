countp = 0
count = 0
counti = 0
somai = 0
while countp < 5 and somai <= 30:
    num = int(input("Digite um numero inteiro: "))
    count += 1
    if num < 0:
        print("Numeros negativos não são aceitos, tente novamente com numeros positivos")
    else:
        if num % 2 == 0:
            p = num
            print(f"{num} é um numero par")
            countp += 1
        else:
            i = num
            somai = somai + num
            print(f"{num} é um numero impar")    
if countp == 5:
    print("\n5 pares")
    print(f"a quantidade de nomeros ímpares foi de: {counti}")
elif somai >= 30:
    print(f"a quantidade de numeros pares foi de: {countp}")
    print(f"a soma dos numeros impares passou de 30, foi: {somai}")

    
