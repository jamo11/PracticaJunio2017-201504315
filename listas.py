class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class pila:
    def __init__(self):
        self.cabeza = None

    def pushPila(self, dato):
        nuevoNodo = nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevoNodo
        else:
            nuevoNodo.siguiente = self.cabeza
            self.cabeza = nuevoNodo

    def pop(self):
        if self.cabeza is not None:
            pop = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            return pop

    def recorrer(self):
        print "Recorrer_________"
        if self.cabeza is not None:
            while self.cabeza is not None:
                print "dato: " + str(self.cabeza.dato)
                self.cabeza = self.cabeza.siguiente

    def operar(self, linea):
        if linea is not None:
            linea = linea.split(" ")
            i = 0
            for l in range(len(linea)):
                if linea[l] == "+" or linea[l] == "-" or linea[l] == "*":
                    self.pushPila(linea[l])
                    print "push: " + linea[l]
                    operador = self.pop()
                    num1 = self.pop()
                    num2 = int(self.pop())
                    res = 0
                    if operador == "+":
                        res = int(num1) + int(num2)
                    elif operador == "-":
                        res = int(num2) - int(num1)
                    elif operador == "*":
                        res = int(num1) * int(num2)
                    print "Resultado: " + str(res)
                    self.pushPila(res)
                else:
                    self.pushPila(linea[l])
                    print "push: " + str(linea[l])
        else:
            print "No hay operaciones en cola"



class cola:
    def __init__(self):
        self.head = None

    def encolar(self, dato):
        nuevoNodo = nodo(dato)
        if self.head is None:
            self.head = nuevoNodo
            nuevoNodo.siguiente = None
        else:
            nodoaux = self.head
            while nodoaux.siguiente is not None:
                nodoaux = nodoaux.siguiente
            nodoaux.siguiente = nuevoNodo

    def desencolar(self):
        if self.head is not None:
            print "dato: " + str(self.head.dato)
            aux = self.head.dato
            self.head = self.head.siguiente
            return aux

    def recorrer(self):
        if self.head is not None:
            nodo = self.head
            while nodo is not None:
                print "Dato de cola: " + str(nodo.dato)
                nodo = nodo.siguiente