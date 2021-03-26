class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=22):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    luiz = Pessoa(nome='Luiz')
    marcos = Pessoa(luiz, nome='Marcos')
    print(Pessoa.cumprimentar(marcos))
    print(id(marcos))
    print(marcos.cumprimentar())
    print('Nome:', (marcos.nome))
    print('Idade:', (marcos.idade))
    for filho in marcos.filhos:
        print(filho.nome)
    marcos.sobrenome = 'Gustavo'
    del marcos.filhos
    marcos.olhos = 1
    del marcos.olhos
    print(luiz.__dict__)
    print(marcos.__dict__)
    print(Pessoa.olhos)
    print(marcos.olhos)
    print(luiz.olhos)
    print(id(Pessoa.olhos), id(marcos.olhos), id(luiz.olhos))
