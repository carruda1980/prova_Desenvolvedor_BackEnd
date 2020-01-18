def recursividade():
    list = [10, 20, 60, 30, 90, 145]
    divisivel = []
    for num in list:
        if num % 2 == 0:
            if num % 3 == 0:
                if num % 10 == 0:
                    divisivel.append(num)
                    print("{} é divisivel por 2,3 e 10".format(num))

    menor = min(m for m in divisivel)
    print("O menor número divisível por 2,3 e 10 é {}".format(menor))

recursividade()