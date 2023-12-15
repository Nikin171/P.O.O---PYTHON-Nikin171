# 1 - Implementar os metodos abaixo para a classe carro:
# a. Ligar Motor
# b. desliga Motor
# c. andar
# d. parar

# 2 - Criar atributos para:
# a. status do motor (ligado/desligado)
# b. status do movimento do carro (andando/parado.)

# 3 - Criar metodos para informar (exibir na tela) o status acima.

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