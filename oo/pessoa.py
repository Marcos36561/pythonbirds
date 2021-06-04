class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=22):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        num1 = 2
        num2 = 2
        resultado = num1 + num2
        return resultado

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = Pessoa.cumprimentar(self)
        return f'{cumprimentar_da_classe}.(Aperto de mão)'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    luiz = Mutante(nome='Luiz')
    marcos = Homem(luiz, nome='Marcos')
    print(Pessoa.cumprimentar(marcos))
    print(id(marcos))
    print(marcos.cumprimentar())
    print('Nome:', (marcos.nome))
    print('Idade:', (marcos.idade))
    for filho in marcos.filhos:
        print(filho.nome)
    marcos.sobrenome = 'Ribeiro'
    del marcos.filhos
    marcos.olhos = 1
    del marcos.olhos
    print(luiz.__dict__)
    print(marcos.__dict__)
    print(Pessoa.olhos)
    print(marcos.olhos)
    print(luiz.olhos)
    print(id(Pessoa.olhos), id(marcos.olhos), id(luiz.olhos))
    print(Pessoa.metodo_estatico(), marcos.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), marcos.nome_e_atributos_de_classe())
    pessoa = Homem('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(luiz, Homem))
    print(luiz.olhos)
    print(marcos.cumprimentar())
    print(luiz.cumprimentar())