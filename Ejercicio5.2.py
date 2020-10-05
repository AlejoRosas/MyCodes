class error:

    def __init__(self,valor):
        self.valor = valor

    def lanzarError(self):
        try:
            if self.valor > 10:
                raise NameError(str(self.valor) + ' es un numero mayor o igual a 10')
        except NameError:
            print('Una excepción ha sido disparada!')
            raise
        except:
            print('Error inesperado!')
        finally:
            print('Gracias por intentarlo...nos vemos pronto')


mydoctor = error(2)
print(mydoctor.lanzarError())