class nodoUsuario():
    def __init__(self, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = contrasena
        self.nodoSiguiente = None
        self.nodoAnterior = None

class listaUsuarios():
    def __init__(self):
        self.cabeza = None

    def addUsuario(self, usuario, contrasena):
        nuevoNodo = nodoUsuario(usuario, contrasena)
        if self.cabeza is None:
            nuevoNodo.nodoSiguiente = nuevoNodo
            nuevoNodo.nodoAnterior = nuevoNodo
            self.cabeza = nuevoNodo
        else:
            nodoAux = self.cabeza.nodoAnterior
            nodoAux.nodoSiguiente = nuevoNodo
            nuevoNodo.nodoSiguiente = self.cabeza
            nuevoNodo.nodoAnterior = nodoAux
            self.cabeza.nodoAnterior = nuevoNodo

    def buscarUsuario(self, usuario, psw):
        print "validando usuario...."
        if self.cabeza is not None:
            aux = self.cabeza.nodoSiguiente
            if usuario == self.cabeza.usuario and psw == self.cabeza.contrasena:
                return True
            else:
                while aux != self.cabeza:
                    if usuario == aux.usuario and psw == aux.contrasena:
                        print("Bienvenido al sistema " + str(usuario))
                        return True
                    aux = aux.nodoSiguiente
                return False
        else:
            return False

    def validarUsuario(self, usuario):
        print "validando nombre de usuario...."
        if self.cabeza is not None:
            aux = self.cabeza.nodoSiguiente
            if usuario != self.cabeza.usuario:
                while aux != self.cabeza:
                    if usuario == aux.usuario:
                        return True
                    aux = aux.nodoSiguiente
            return False
        else:
            return False

    def recorrer(self):
        aux = self.cabeza.nodoSiguiente
        print "usuario: "+ str(self.cabeza.usuario)
        while aux != self.cabeza:
            print "usuario: " + str(aux.usuario)
            aux = aux.nodoSiguiente


class Main:
    def _init_(self):
        self.op = None

    def crearUsuario(self):
        psw = ""
        nombre = raw_input("Ingrese nombre de usuario a crear: ")
        if lista.validarUsuario(nombre) is False:
            psw = raw_input("Ingrese contrasena de usuario: ")
            lista.addUsuario(nombre, psw)
            lista.recorrer()
        else:
            print ("Usuario ya existe")
            self.menuPrincipal()

    def menuPrincipal(self):
        print("""
            Alumno: Jose Andres Martinez Ovando
            Carnet: 201504315
            ______________________________________________________

            Menu Principal:
            1. Crear Usuario
            2. Ingresar al Sistema
            3. Salir del Programa

            Ingrese una opcion:
        """)

        op = input()
        if op == 1:
            print "Crear Usuario"
            self.crearUsuario()
            self.menuPrincipal()
        elif op == 2:
            print "Ingresar al Sistema"
            usuario = raw_input("Ingrese el usuario:")
            if lista.buscarUsuario(usuario, raw_input("Ingrese contrasena:")):
                self.menuSistema()
            else:
                print "El usuario o contrasena no es correcto.."
                self.menuPrincipal()
        elif op == 3:
            print "Salir del Programa"

    def menuSistema(self):
        print("""
            Opciones del Sistema:
            1. Leer Archivo
            2. Resolver Operaciones
            3. Operar Matriz
            4. Mostrar Usuarios
            5. Mostrar Cola
            6. Cerrar Sesion

            Ingrese una opcion:
        """)
        sistema = input()

        if sistema == 1:
            print "LEER ARCHIVO"
        elif sistema == 2:
            print """
                1. Operar Siguiente
                2. Regresar
                
                Elija una opcion..
            """
            if(raw_input() == 2):
                self.menuSistema()
            else:
                print "operar siguiente en cola"
        elif sistema == 3:
            print """
                1. Ingresar Dato
                2. Operar Transpuesta
                3. Mostrar Matriz Original
                4. Mostrar Matriz Transpuesta
                5. Regresar
                
                Elija una opcion..
            """
            opcion = raw_input()
            if(opcion == 1):
                print "INGRESAR DATO"
            elif (opcion == 2):
                print "OPERAR TRANSPUESTA"
            elif (opcion == 3):
                print "ORIGINAL"
            elif (opcion == 4):
                print "TRANSPUESTA"
            elif (opcion == 5):
                print "REGRESAR"
                self.menuSistema()
        elif sistema == 4:
            print "MOSTRAR USUARIOS"
            lista.recorrer()
        elif sistema == 5:
            print "MOSTRAR COLA DE OPERACIONES"

        elif sistema == 6:
            self.menuPrincipal()

lista = listaUsuarios()
main = Main()
main.menuPrincipal()
