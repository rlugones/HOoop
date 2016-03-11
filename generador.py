"""
Un generador de senal es el responsable de generar una senal portadora.
"""

class Generador(object):

    def __init__(self, amplitud, fase, frecuencia):
        self.amplitud = amplitud
        self.fase = fase
        self.frecuencia = frecuencia

        #  muestras por segundo
        self.frecuencia_muestreo = frecuencia*3


    def generar(self, tiempo_inicial, tiempo_final):

        import numpy as np

        cantidad_muestras = int((tiempo_final - tiempo_inicial).seconds/\
        self.frecuencia_muestreo)

        muestras = np.arange(cantidad_muestras)
        ruido_blanco = np.random.normal(0,1,cantidad_muestras) * self.amplitud/10

        ret = self.amplitud*np.sin(2*(1/self.frecuencia)*muestras+self.fase) + \
                ruido_blanco

        return ret
