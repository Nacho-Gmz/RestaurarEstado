import pickle

# Clase Contacto
class Contacto:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero

    def __str__(self):
        return f"{self.nombre}: {self.numero}"

# Clase Agenda
class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, numero):
        self.contactos.append(Contacto(nombre, numero))

    def ver_contactos(self):
        for c in self.contactos:
            print(c)

    def guardar_en_archivo(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump(self.contactos, f)

    def cargar_desde_archivo(self, archivo):
        with open(archivo, 'rb') as f:
            self.contactos = pickle.load(f)

# Uso de la clase Agenda
agenda = Agenda()
opc = 0
print("Agenda de contactos")
print("Opciones:")
print("1. Agregar contacto")
print("2. Ver contactos")
print("3. Cargar contactos")
print("4. Salir")
print("Los contactos se guardan cada que agregas uno nuevo")

while opc != 4:
    opc = int(input("Ingrese una opcion: "))

    if opc == 1:
        nombre = input("Nombre:")
        numero = input("Numero:")
        agenda.agregar_contacto(nombre, numero)
        agenda.guardar_en_archivo("agenda.pickle")
        print("Contacto agregado exitosamente")
    elif opc == 2:
        agenda.ver_contactos()
    elif opc == 3:
        agenda.cargar_desde_archivo("agenda.pickle")
        print("Agenda importada correctamente")
    elif opc == 4:
        print("Adios")
    else:
        print("Opcion invalida")
