class Detector(object):

    def __init__(self,umbral):
        self.umbral = umbral
        pass

    def detectar(self, senal):
        deteccion = False
        if max(senal) > self.umbral : deteccion = True
        return deteccion
