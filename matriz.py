class nodoMatriz:
    def __init__(self, dato):
        self.derecha
        self.izquierda
        self.arriba
        self.abajo
        self.dato = dato
        self.inicial

class matriz:
    def crearmatriz(self, x, y):
        if self.inicial is None:
            nuevoNodo = nodoMatriz(0)
            self.inicial = nuevoNodo
        else:

            aux = self.inicial
            temp = aux
            for i in range (1, y-1):
                for j in range(1, x-1):
                    if i == 1:
                        nuevoNodo = nodoMatriz(0)
                        aux.derecha = nuevoNodo
                        nuevoNodo.izquierda = aux
                        aux = nuevoNodo
                    else:
                        nuevoNodo = nodoMatriz(0)
                        nuevoNodo.arriba = temp
                        aux.derecha = nuevoNodo
                        nuevoNodo.izquierda = aux
                        aux = nuevoNodo


                temp = temp.abajo