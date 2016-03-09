class Medio(object):

    def __init__(self, blancos):
        self.blancos = blancos

    def refractar(self, una_senal, tiempo_inicial, tiempo_final):
        """
        Los blancos en el medio reflejan la senal
        """
        import numpy as np
        senal_reflejada = np.zeros(len(una_senal))
        amplitud_medio = 0.6
        for i in self.blancos:
            senal_reflejada += i.reflejar(amplitud_medio*una_senal,\
                tiempo_inicial, tiempo_final)
        return senal_reflejada
