class Detector(object):

    def __init__(self):
        #TODO: completar con la inicializacion de los parametros del objeto
        pass

    def detectar(self, senal):
        deteccion = False
        if max(senal)>0.1 : deteccion = True
        return deteccion
