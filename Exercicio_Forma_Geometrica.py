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
#Calcular area do retangulo com função area e funcao perimetro:
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
    print('Os Lados são iguais. Isso é um quadrado sua anta!!')
else:
  
    print("A área do retangulo é:", ret.area)
    print("O perímetro do retangulo é:", ret.perimetro)
'''
#Calcular area do circulo com função area, perimetro e diametro:
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
#Calcular area do triangulo com função base e altura:
'''
class triangulo():
  def __init__(self, base, altura, lado_a=2, lado_b=3, lado_c=5, angulo_ab=90, angulo_ac=30, angulo_bc=60):
    
        self.__base = base 
        self.__altura = altura
        self.__lado_a = lado_a
        self.__lado_b = lado_b
        self.__lado_c = lado_c
        self.__angulo_ab = angulo_ab
        self.__angulo_ac = angulo_ac
        self.__angulo_bc = angulo_bc 

  @property
  def base(self):
      return self.__base
    
  @property
  def altura(self):
      return self.__altura
    
  @property
  def lado_a(self):
    return self.__lado_a

  @property
  def lado_b(self):
    return self.__lado_b
    
  @property
  def lado_c(self):
    return self.__lado_c

  @property
  def angulo_ab(self):
    return self.__angulo_ab
    
  @property
  def angulo_ac(self):
    return self.__angulo_ac
    
  @property
  def angulo_bc(self):
    return self.__angulo_bc

  @property 
  def area(self):
    return (self.__base * self.__altura) / 2
 
  @property
  def perimetro(self):
    return self.__lado_a + self.__lado_b + self.__lado_c

  @property
  def tipo_triangulo(self):
    if self.__lado_a == self.__lado_b and self.__lado_b == self.__lado_c:
        return 'triangulo equilatero'
    elif self.__lado_a == self.__lado_b or self.__lado_a == self.__lado_c:  
        return 'triangulo isóceles'
    else:
        return 'triangulo escaleno'
        
t = triangulo(10, 10, 10, 10, 10)
print(t.tipo_triangulo)
'''
