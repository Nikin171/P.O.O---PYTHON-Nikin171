#Considere as classes ContaCorrente e Poupança apresentadas em sala de aula. Crie uma classe ContaImposto que herda de conta e possui um atributo percentualImposto.
#Esta classe tambem possui um metodo calculaImposto que subtrai do saldo, o valor do proprio saldo multiplicado pelo percentual do imposto. Crie um programa para criar
#objetos, testar todos os metodos e exibir atributos das 3 classes (ContaCorrente, Poupança e ContaImposto)

class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

class ContaCorrente(Conta):
    pass

class Poupanca(Conta):
    pass

class Conta_Imposto(Conta):
    def __init__(self, saldo, percentual_Imposto):
        super().__init__(saldo) # Super é uma forma de herdar a classe conta para as subclasses que são conta corrente, poupança e conta imposto.
        self.percentual_Imposto = percentual_Imposto

    def calcula_Imposto(self):
        self.saldo -= self.saldo * self.percentual_Imposto

# Objetos
conta_corrente = ContaCorrente(200)
poupanca = Poupanca(5000)
conta_imposto = Conta_Imposto(200, 0.10)

# Métodos
conta_imposto.calcula_Imposto()

# Atributos
print(f"Saldo Conta Corrente: {conta_corrente.saldo}")
print(f"Saldo Poupança: {poupanca.saldo}")
print(f"Saldo Conta Imposto: {conta_imposto.saldo}")
