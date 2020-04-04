class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanzar(self):
        print('Estoy caminando')

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanzar(self):
        print('Voy en Bicicleta')

def main():
    persona = Persona('Gerson')
    persona.avanzar()
    ciclista = Ciclista('Mario')
    ciclista.avanzar()

if __name__ == "__main__":
    main()