from funciones_proyecto_datos import *
usuario = ""
nombre = ""
apellido = ""
correo = ""
contrasena = ""

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
    while condiciones_ciclo == False:
        usuario = introducir_usuario()
        nombre = introducir_nombre()
        apellido = introducir_apellido()
        correo = introducir_correo()
        contrasena = introducir_contrasena()
        confirmar_datos()
        
    guardar_datos()  
        
    
#Mas informacion:
elif respuesta_info == "3":
    print "==============\n<> PROYECTO CREADO POR: itskaru_\n=============="
    
#Respuesta dada al no ser reconocida la respuesta.
else:
    print "=============="
    print "La respuesta no es valida."
    print "=============="