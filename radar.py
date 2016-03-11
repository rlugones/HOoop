import matplotlib.pyplot as plt
import numpy as np


"""
Define el similador del Radar
"""

class Radar(object):

    def __init__(self, generador, detector):
        self.generador = generador
        self.detector = detector

    def detectar(self, medio, tiempo_inicial, tiempo_final):
        """
        Detecta si hay un blanco en un medio, en un intervalo de tiempo.
        """
        una_senal = self.generador.generar(tiempo_inicial, tiempo_final)
        una_senal_reflejada = medio.refractar(una_senal, tiempo_inicial, \
                                            tiempo_final)
        return self.detector.detectar(una_senal_reflejada),\
            una_senal, una_senal_reflejada

    def plotear_senal(self, senal_inicial, senal_final):
        """
        Plotea las senales generada y recibida
        """
        x=np.arange(len(senal_inicial))
        f=plt.figure()
        ax=f.add_subplot(111)
        ax.plot(x,senal_inicial,label='senal generada')
        ax.plot(x,senal_final,label='senal recibida')
        ax.set_ylabel('Senal')
        ax.legend()
        plt.show()
