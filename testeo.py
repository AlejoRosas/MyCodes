import unittest
import prueba

class TestMyModule(unittest.TestCase):  #testjuego definiciones

    def test_agregarTiempo(self):
        self.assertTrue(prueba.agregarTiempo(6))
        self.assertRaises(TypeError, prueba.agregarTiempo,6, "python")


    def test_sum(self):
        self.assertEqual(prueba.sum(5,7),12)
        self.assertRaises(TypeError,prueba.sum,5, "python")

    def test_guardarConcepto(self):
        concepto = "concepto"
        self.assertEqual(prueba.guardarConcepto(concepto),"Guardado exitoso")
        self.assertTrue(prueba.buscarConcepto(concepto))

    def test_guardarDefinicion(self):
        definicion= "definicion"
        self.assertEqual(prueba.guardarDefinicion(definicion),"Guardado Exitoso")
        #self.assertTrue(prueba.buscarDefinicion(definicion))

    def test_buscarConcepto(self):
        concepto = "concepto"
        self.assertTrue(prueba.buscarConcepto(concepto))

    def test_buscarDefinicion(self):
        definicion = "definicion"
        self.assertTrue(prueba.buscarDefinicion(definicion))


    def test_eliminarConcepto(self):
        concepto = "concepto"
        self.assertEqual(prueba.eliminarConcepto(concepto),"Eliminado con exito")
        self.assertFalse(prueba.buscarConcepto(concepto))

    def test_eliminaDefinicion(self):
        definicion  = "definicion"
        self.assertEqual(prueba.eliminarDefinicion(definicion),"Eliminado con exito")
        self.assertFalse(prueba.buscarDefinicion(definicion))

    #La funcion debe retornar un valor verdadero tras crear el listado de definiciones
    def test_listado(self):
        self.assertTrue(prueba.listado())

    def test_almacenarCantTiempo(self):
        cantidad = 3
        self.assertTrue(prueba.almacenarCantidad(cantidad))

    def test_almacenarCantPreguntas(self):
        cantidad = 4
        self.assertTrue(prueba.almacenarCantPreguntas(cantidad))

if __name__=="__main__":
    unittest.main()