import datetime
#import numpy as np
import matplotlib.pyplot as plt
import radar
import medio
import blanco
import generador
import detector
import blancoCluter


# DISCLAMER!!
# todo esta en castellano por razones didacticas
# pero DEBEN programar en INGLES
# uno nunca sabe quien puede leer su codigo

def main():

    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)

    import math
    # parametros del generador de senales
    amplitud = 1#0.2
    fase = 1
    frecuencia = 5*math.pi #20

    generador1 = generador.Generador(amplitud, fase, frecuencia)
                        ### construir un nuevo genrador de senales

    detector1 = detector.Detector()
                        ### construir un detector

    radar1 = radar.Radar(generador1, detector1) ### construir un nuevo radar

    # parametros para un blanco
    amplitud_de_frecuencia_del_blanco = 0.14 #amplitud + 100
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)
    blanco1 = blanco.Blanco(amplitud_de_frecuencia_del_blanco,\
        tiempo_inicial_del_blanco,\
        tiempo_final_del_blanco)  #TODO contruir un nuevo blanco
    blanco2 = blanco.Blanco(0*amplitud_de_frecuencia_del_blanco,\
        tiempo_inicial_del_blanco,\
        tiempo_final_del_blanco)  #TODO contruir un nuevo blanco
    blanco3 = blancoCluter.Blancocluter(amplitud_de_frecuencia_del_blanco,\
        tiempo_inicial,\
        tiempo_final)  #TODO contruir un nuevo blanco


    medio1 = medio.Medio([blanco3])  #TODO contruir un medio

    [deteccion,senal_inicial,senal_final] = radar1.detectar(medio1, tiempo_inicial, tiempo_final)  #TODO construir un radar
    if deteccion:
        print('Se detecta una senal.')
    else:
        print('No se detecta una senal.')

    radar1.plotear_senal(senal_inicial,senal_final)

if __name__ == "__main__":
    main()
