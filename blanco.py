import numpy as np

class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        self.amplitud = amplitud
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final

    def reflejar(self, senal, tiempo_inicial, tiempo_final):
        """
        Reflexión de la senal en el blanco
        """
        frec_muestreo = float(len(senal)) / (tiempo_final-tiempo_inicial).seconds
        pos_inicial = frec_muestreo * (self.tiempo_inicial-tiempo_inicial).seconds
        pos_final = frec_muestreo * (self.tiempo_final-tiempo_inicial).seconds
        senal_reflejada = np.zeros(len(senal))
        senal_reflejada[pos_inicial:pos_final] = \
                senal[pos_inicial:pos_final] * self.amplitud
        return senal_reflejada
