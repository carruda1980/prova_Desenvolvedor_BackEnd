def soma(numero):
    soma = sum(x for x in range(numero) if x % 3 == 0 or x % 5 == 0)
    print(soma)


soma(1000)


