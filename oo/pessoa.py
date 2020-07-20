class Pessoa:
    def __init__(self, *filhos, nome=None, idade=44):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'ola {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo') # filho de luciano
    luciano = Pessoa(renzo,nome='Luciano')
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    #print(luciano.filhos)
    print('filhos...')
    for filho in luciano.filhos:
        print(filho.nome)
