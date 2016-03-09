import blanco

class Blancocluter(blanco.Blanco):
    """
    Define un Blancocluter a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        super().__init__(20*amplitud, tiempo_inicial, tiempo_final)
        #self.amplitud *= 20
        ##TODO: completar con la inicializacion de los parametros del objeto
        #pass

#    def reflejar(self, senal, tiempo_inicial, tiempo_final):

        #TODO ver como se encajan los timepos del blanco y del intervalo de tiempo
        # senal.insert(self.instante, senal[instante]+self.amplitud)
        # modificar la senal conlos parametros del blanco
#        pass
