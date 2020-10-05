class vertebrado():
    atribute = "vertebrado"

    def funcion(self):
        print("vertebrado")
        return self.atribute
class anfibio():
    atribute = "anfibio"

    def funcion(self):
        print("anfibio")
        return self.atribute
class terrestre():
    atribute = "terrestre"

    def funcion(self):
        print("terrestre")
        return self.atribute
class oviparo():
    atribute = "oviparo"

    def funcion(self):
        print("oviparo")
        return self.atribute
class mamifero():
    atribute = "mamifero"

    def funcion(self):
        print("mamifero")
        return self.atribute

class perro(terrestre,mamifero,vertebrado):
    def funcion(self):
        print("soy un",anfibio.atribute, " un ",mamifero.atribute, " y un ", vertebrado.atribute)

class rana(anfibio,oviparo):
    def funcion(self):
        print("soy un", anfibio.atribute, "y un ", oviparo.atribute)


bolt = perro()
rinrin = rana()

rinrin.funcion()
bolt.funcion()