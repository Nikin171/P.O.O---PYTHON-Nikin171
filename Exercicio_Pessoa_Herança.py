class Pessoa:
    def __init__(self, nome, idade, endereço, cpf, sexo):

        self.__nome = nome
        self.__idade = idade
        self.__endereço = endereço
        self.__cpf = cpf 
        self.__sexo = sexo 

    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def endereço(self):
        return self.__endereço
    @property
    def cpf(self):
        return self.__cpf
    @property
    def sexo(self):
        return self.__sexo


class Pai(Pessoa): 
     
    def __init__(self, nome, idade, endereço, cpf, sexo):
        super().__init__(nome, idade, endereço, cpf, sexo)

p = Pai('Elcimar /', 55, '/ Rua H-70 / ', '***.***.***-01', '/ Sexo: Masculino')
print(p.nome, p.idade, p.endereço, p.cpf, p.sexo)

class Mae(Pessoa): 
     
    def __init__(self, nome, idade, endereço, cpf, sexo):
        super().__init__(nome, idade, endereço, cpf, sexo)

m = Mae('Neide /', 54, '/ Rua H-89 / ', '***.***.***-55', '/ Sexo: Feminino')
print(m.nome, m.idade, m.endereço, m.cpf, m.sexo)
        
class Filho(Pessoa): 
     
    def __init__(self, nome, idade, endereço, cpf, sexo):
        super().__init__(nome, idade, endereço, cpf, sexo)

f = Filho('Nickollas /', 28, '/ Rua H-89 / ', '***.***.***-70', '/ Sexo: Masculino')
print(f.nome, f.idade, f.endereço, f.cpf, f.sexo)