#Numero par ou impar
'''
def numero_par_ou_ímpar(numero):
    if numero % 2 == 0:
        return f'O número {numero} é par.'
    return f'O número {numero} é ímpar.'

numero = int(input('Informe um número inteiro qualquer: '))
print(numero_par_ou_ímpar(numero))
'''
#Como calcular area do quadrado com função area e funcao perimetro:
'''
class Quadrado:
  def __init__(self, lado):
    self._lado = lado

  @property
  def lado(self):
    return self._lado
  
  def area(self):
    return self._lado ** 2

  def perimetro(self):
    return 4 * self._lado

lado = int(input("Digite o lado do quadrado: "))

quadrado = Quadrado(lado)

print("A área do quadrado é:", quadrado.area())
print("O perímetro do quadrado é:", quadrado.perimetro())
'''
#Calcular area do retangulo com função area e funcao perimetro em python
'''
class retangulo:
  def __init__(self, lado1, lado2):
    self.lado1 = lado1
    self.lado2 = lado2

  @property
  def area(self):
    return self.lado1 * self.lado2

  @property
  def perimetro(self):
    return 2 * self.lado1 + 2 * self.lado2

lado1 = int(input("Digite o lado 1 do retangulo: "))
lado2 = int(input("Digite o lado 2 do retangulo: "))

ret = retangulo(lado1,lado2)

if lado1 == lado2:
    print('Os Lados são iguais. Isso é um quadrado fi de rapariga...')
else:
  
    print("A área do retangulo é:", ret.area)
    print("O perímetro do retangulo é:", ret.perimetro)
'''

#Calcular area do circulo com função area e funcao diametro em python:
'''
from math import pi

class Circulo():
    def __init__(self, raio):
        self.__raio = raio
    
    @property
    def raio(self):
        return self.__raio
    
    @property
    def perimetro(self):
        return 2 * pi * self.__raio
    
    @property
    def diametro(self):
        return self.__raio * 2
    
    @property
    def area(self):
        return pi * self.__raio * self.__raio
    
    raio = float(input('Digite o raio do circulo: '))
c = Circulo(raio)
print(c.diametro)
'''

#Calcular area do triangulo com função area e funcao diametro em python:

class triangulo():
    def area(base, altura):
        return base * altura / 2
    def diametro(raio):
        return 2 * raio
    
    base = float(input('Digite a base do triângulo: '))
    altura = float(input('Digite a altura do triângulo: '))

    area_triangulo = area(base, altura)
    diametro_circulo = diametro(base / 2)
    
    if base == altura:
            print(f'Quando todos os lados são congruentes é um triângulo equilátero.')

    else:
        print(f'A area do triângulo é: ', area_triangulo)
        print(f'O diametro do circulo é: ', diametro_circulo)
