# prompt: criar uma classe de pessoa, que tenha como atributos: nome, nascimento, cpf, rg, endereço, completo e estado civil, 
# e que tenha como comportamento o calculo da idade, e outro que retorne todos os dados da pessoa formatados (da forma como achar melhor) 
# detalhe: a idade nao é fornecida, mas sim calculada com base na data de hoje..
'''
from datetime import datetime

class Pessoa:
    def __init__(self, nome, nascimento, cpf, rg, endereco, estado_civil):
        self.nome = nome
        self.nascimento = datetime.strptime(nascimento, '%d/%m/%Y')
        self.cpf = cpf
        self.rg = rg
        self.endereco = endereco
        self.estado_civil = estado_civil

    def calcular_idade(self):
        hoje = datetime.now()
        idade = hoje.year - self.nascimento.year - ((hoje.month, hoje.day) < (self.nascimento.month, self.nascimento.day))
        return idade

    def obter_dados_formatados(self):
        dados_formatados =  f"Nome: {self.nome}\n"\
                            f"Nascimento: {self.nascimento.strftime('%d/%m/%Y')}\n"\
                            f"CPF: {self.cpf}\n"\
                            f"RG: {self.rg}\n"\
                            f"Endereço: {self.endereco}\n"\
                            f"Estado Civil: {self.estado_civil}\n"\
                            f"Idade: {self.calcular_idade()} anos"
        return dados_formatados

# Exemplo de como usar:
pessoa_exemplo = Pessoa("João Da Silva", "15/05/1990", "123.456.789-00", "1234567-8", "Rua Perimetral, 1995", "Solteiro")
print(pessoa_exemplo.obter_dados_formatados())
'''
# 1-implementar os metodos abaixo para a classe carro:
# a. Ligar Motor
# b. desliga Motor
# c. andar
# d. parar

# 2-criar atributos para:
# a. status do motor (ligado/desligado)
# b. status do movimento do carro (andando/parado.)

# 3-criar metodos para informar (exibir na tela) o status acima.

class Carro:
    def __init__(self):
        self.motor_ligado = False
        self.movimento = "parado"

    def ligar_motor(self):
        if not self.motor_ligado:
            self.motor_ligado = True
            print("Motor ligado.")
        else:
            print("O motor já está ligado.")

    def desligar_motor(self):
        if self.motor_ligado:
            self.motor_ligado = False
            print("Motor desligado.")
        else:
            print("O motor já está desligado.")

    def andar(self):
        if self.motor_ligado and self.movimento == "parado":
            self.movimento = "andando"
            print("O carro está em movimento.")
        elif self.movimento == "andando":
            print("O carro já está em movimento.")
        else:
            print("Ligue o motor antes de começar a andar.")

    def parar(self):
        if self.movimento == "andando":
            self.movimento = "parado"
            print("O carro parou.")
        elif self.movimento == "parado":
            print("O carro já está parado.")
        else:
            print("O carro não está em movimento.")

    def exibir_status(self):
        print(f"Status do motor: {'Ligado' if self.motor_ligado else 'Desligado'}")
        print(f"Status do movimento: {self.movimento}")


# Exemplo de uso
carro = Carro()

carro.exibir_status()
carro.ligar_motor()
carro.exibir_status()
carro.andar()
carro.parar()
carro.desligar_motor()
carro.exibir_status()

