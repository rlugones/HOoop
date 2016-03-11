import blanco

class Blancocluter(blanco.Blanco):
    """
    Define un Blancocluter a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        super().__init__(20*amplitud, tiempo_inicial, tiempo_final)
