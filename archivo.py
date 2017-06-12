from xml.dom import minidom
import listas
import usuarios

cola = listas.cola()
class archivo:
    def __init__(self):
        self.xml = None

    def leerarchivo(self, ruta):
        xml = minidom.parse(ruta)
        # print archivo.toxml()
        itemlist = xml.getElementsByTagName("x")
        for i in itemlist:
            print (i.firstChild.nodeValue)

        itemlist2 = xml.getElementsByTagName("y")
        for i in itemlist2:
            print (i.firstChild.nodeValue)

        itemlist3 = xml.getElementsByTagName("operacion")
        for i in itemlist3:
            cola.encolar(i.firstChild.nodeValue.strip())
        global new
        new = cola

    def imprimircola(self):
        listas.cola.recorrer()

# C:\Users\Andres\Desktop\UNIVERSIDAD\EDD\prueba_edd.xml