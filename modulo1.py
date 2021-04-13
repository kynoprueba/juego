class Humano():
    def __init__(self, edad ,idioma,cantar):
        self.edad=edad
        self.idioma=idioma
        self.cantar=cantar

    def hablar(self,mensaje):
       print(mensaje)

    def lenguas(self):
        print(self.idioma)

    def deportes(self):
        lista=['futbol','ciclismo','basket']
        print(lista[2])


class Musico(Humano):
    print('hola mundo')


class Ingeniero(Humano):
    def calcular(self,software):
        return software


class Estudioso(Musico,Ingeniero):
    pass


