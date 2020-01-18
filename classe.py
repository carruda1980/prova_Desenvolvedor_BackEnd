class Produto(object):
    def __init__(self, numero1, numero2, numero3):
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3

    def multiplica(self):
        return self.numero1 * self.numero2 * self.numero3

produto = Produto(10,2,40)
print(produto.__dict__) # valores iniciais
produto.numero1 = 65
produto.numero3 = 20
produto.numero3 = 500
print(produto.__dict__) # novos valores
print(produto.multiplica()) # novos multiplicados
