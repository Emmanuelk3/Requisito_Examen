listaAlumnos = []

class Estudiantes(object):
    def __init__(self, _matricula, _nombre, _apellido,_Examen1, _Examen2, _Pia):
        self.matricula = _matricula
        self.nombre = _nombre
        self.apellido = _apellido
        self.examen1 = _Examen1
        self.examen2 = _Examen2
        self.pia = _Pia
        self.notaFinal = (_Examen1 + _Examen2 + _Pia)/3
    def darDatos(self):
        print("No. Mat ricula: {} - {} {} - Nota Final: {}".format(self.matricula, self.nombre, self.apellido, self.notaFinal))


def registrarEstudiante():
    print("Registro de Estudiantes\n")
    matricula = int(input("Ingrese el numero de matricula: "))
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingrese tu apellido: ")
    examen1 = float(input("Ingresea tu calificacion  del Examen1: "))
    examen2 = float(input("Ingresa tu calificacion del Examen 2: "))
    pia = float(input("Ingrese tu calificacion del pia: "))
    objAlumno = Estudiantes(matricula, nombre, apellido, examen1, examen2, pia)
    listaAlumnos.append(objAlumno)

def listadoEstudiantes():
    print("Listado de Estudiantes\n")
    for objAlumno in listaAlumnos:
        objAlumno.darDatos()

def buscarEstudiante():
    print("Buscar Estudiante\n")
    Matricula = int(input("Ingrese el numero de matricula buscar: "))
    for objAlumno in listaAlumnos:
        if Matricula == objAlumno.matricula:
            objAlumno.darDatos()

def salir():
    print("Usted salio!")
    exit()

def main():
    while True:
        print("\n")
        print("|°°°°°°°°°°°°°°°°°°°°°°°°°°°°|")
        print("|        ¡Bienvenidos!       |")
        print("|           Menu             |")
        print("|°°°°°°°°°°°°°°°°°°°°°°°°°°°°|")
        print("")
        print("Eliga una de las siguientes opciones:")
        print("1.- Registrar Estudiante")
        print("2.- Ver Estudiantes")
        print("3.- Buscar Estudiante")
        print("4.- Salir\n")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            registrarEstudiante()
        elif opcion == 2:
            listadoEstudiantes()
        elif opcion == 3:
            buscarEstudiante()
        elif opcion == 4:
            salir()

if __name__ == '__main__':
   main()