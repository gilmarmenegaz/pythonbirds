class Pessoa:
    def __init__(self,nome=None, idade=44):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'ola {id(self)}'


if __name__ == '__main__':
    p = Pessoa('teste')
    #print(Pessoa.cumprimentar((p)))
    #print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'atrualiza teste'
    print(p.nome)
