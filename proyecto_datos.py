from funciones_proyecto_datos import *

#PRINCIPAL:
#Menu para introducir respuesta.
respuesta_info = raw_input(
    "==============\nPara buscar informacion pulse: [1].\nPara aportar nuevos datos introduzca: [2].\nPara obtener otra informacion introduzca: [3].\n==============\nRespuesta: ")

#Buscar datos:
if respuesta_info == "1":
    buscar_datos()

#Introducir datos:
elif respuesta_info == "2":
    print "=============="
    condiciones_ciclo = False
    while condiciones_ciclo == False:
        introducir_usuario()
        introducir_nombre()
        introducir_apellido()
        introducir_correo()
        introducir_contrasena()
        condiciones_ciclo = confirmar_datos()

    guardar_datos()


#Mas informacion:
elif respuesta_info == "3":
    print "==============\n<> PROYECTO CREADO POR: itskaru_\n=============="

#Respuesta dada al no ser reconocida la respuesta.
else:
    print "=============="
    print "La respuesta no es valida."
    print "=============="
