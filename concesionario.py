class Concesionario():
    def __init__(self):

        self.myInventario = InventarioDeAutos()
        self.myCatalogo = Catalogo()

    def registrarMarca(self,marca):
        if marca != None or marca != " ":
            self.myInventario.listaMarca.append(marca)

    def getCantidad(self):
        return len(self.myInventario.listaMarca)

    def getPrecio(self,marca):
        if marca in self.myCatalogo.listaMarca:
            return self.listaMarca[marca]

class Catalogo():
    def __init__(self):
        self.listaPrecio = ["20000", "50000"]
        self.listaMarca = ["audi", "toyota"]

    def getPrecio(self, marca):
        if marca in self.listaMarca:
            pos=self.listaMarca.index(marca)
            return self.listaPrecio[pos]

class InventarioDeAutos():
    def __init__(self):
        self.listaMarca = ["audi", "toyota"]

    def mostrasrLista(self):
        print(self.listaMarca)

