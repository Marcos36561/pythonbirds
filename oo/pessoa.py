class Pessoa:
    def __init__(self, nome=None, idade=22):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Marcos')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print('Nome:',(p.nome))
    print('Idade:',(p.idade))
    p.nome = 'Luiz'
    print(p.nome)
