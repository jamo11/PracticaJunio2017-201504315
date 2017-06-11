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
            print "dato: " + str(self.cabeza.dato)
            self.cabeza = self.cabeza.siguiente

    def recorrer(self):
        if self.cabeza is not None:
            while self.cabeza is not None:
                print "dato: " + str(self.cabeza.dato)
                self.cabeza = self.cabeza.siguiente

pila = pila()


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
            self.head = self.head.siguiente

    def recorrer(self):
        if self.head is not None:
            nodo = self.head
            while nodo is not None:
                print "dato: " + str(nodo.dato)
                nodo = nodo.siguiente

cola = cola()
