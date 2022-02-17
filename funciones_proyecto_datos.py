import string
import json

#VARIABLES GLOBALES:
datos_lista_raw = []
datos_lista = {}
condiciones_ciclo = False
usuario = ""
nombre = ""
apellido = ""
correo = ""
contrasena = ""

ruta_txt = "PROYECTO DATOS [python]\\archivo_proyecto_datos.txt"
ruta_json = "PROYECTO DATOS [python]\\archivo_proyecto_datos_json.json"

#FUNCIONES:
#Adquire los datos del archivo TXT.
def adquirir_datos_txt():  
    #Abre el archivo en modo READ y guarda su informacion (linea por linea) en una variable.
    archivo_completo = []
    with open(ruta_txt, "r") as archivo_txt:
        archivo_completo = archivo_txt.readlines()

    #Quita los saltos de linea del archivo.
    archivo_final = []
    for p in archivo_completo:
        archivo_final += [p.replace("\n", "").replace("=", "")]
    return archivo_final



#Busca los datos en el archivo TXT.
def buscar_datos():
    archivo_final = adquirir_datos_txt()
    ciclo_buscar_info = False   
    print "=============="
    respuesta_buscar_info_raw = raw_input("Introduzca el usuario a buscar: ")
    respuesta_buscar_info = "USUARIO: " + respuesta_buscar_info_raw
    #Inicia un bucle por cada frase del programa comprando el nombre introducido.
    for info in archivo_final:
        if ciclo_buscar_info == True:
            print info
            break
        if info == respuesta_buscar_info:
            ciclo_buscar_info = True
    print "=============="

    #Si no encuentra resultado hace un PRINT de esto.
    if ciclo_buscar_info == False:
        print "No se han encontrado resultados."
        print "=============="       



#Introducir el usuario junto a sus condiciones.
def introducir_usuario():
    archivo_final = adquirir_datos_txt()
    longuitud_nombre_usuario = 5
    condiciones_usuario = False
    #Comprueba si la longutud del usuario es mayor que la establecida.
    while condiciones_usuario == False:
        usuario = raw_input("Escriba su usuario: ")
        if len(usuario) < longuitud_nombre_usuario:
            print "La longuitud del usuario no puede ser menor a {0}.".format(longuitud_nombre_usuario)
            print "=============="
            condiciones_usuario = False
        else:
            condiciones_usuario = True
            #Se establece las condiciones en TRUE y si al final del ciclo el usuario ya esta registrado lo cambia a FALSE.
            #Si el usuario ya esta registrado hace un PRINT y establece las condiciones a FALSE.
            for usuario_registrado in archivo_final:
                if ("USUARIO: " + usuario) == usuario_registrado:
                    condiciones_usuario = False
                    print "El usuario ya esta registrado."
                    print "=============="
                    break
    print "=============="
    return usuario



#Introdcir el nombre junto a sus condiciones.
def introducir_nombre():
    condiciones_nombre = False    
    while condiciones_nombre == False:
            nombre = raw_input("Escriba su nombre: ")
            for letra in nombre:
                if letra in string.digits:
                    print "El nombre no puede contener numeros."
                    print "=============="
                    condiciones_nombre = False
                    break
                condiciones_nombre = True
    print "=============="
    return nombre



#Introdcir el apellido junto a sus condiciones.
def introducir_apellido():
    condiciones_apellido = False
    while condiciones_apellido == False:
            apellido = raw_input("Escriba su apellido: ")
            for letra in apellido:
                if letra in string.digits:
                    print "El apellido no puede contener numeros."
                    print "=============="
                    condiciones_apellido = False
                    break
                condiciones_apellido = True
    print "=============="
    return apellido



#Hacer un check del correo para comprobar si es legitimo.
def check_email(correo):
    #Separa el correo en dos partes desde la arroba para obtener el dominio.
    correo_separado_desde_arroba = correo.split("@")

    #Se crea una variable que guarde el dominio del correo.
    dominio_correo = correo_separado_desde_arroba[1]

    #Separa el dominio y el TLD.
    dominio_correo_separado = dominio_correo.split(".")

    #Separa en dos variables el dominio.
    parte_arroba_correo = dominio_correo_separado[0]
    parte_punto_correo = dominio_correo_separado[1]

    if parte_arroba_correo.isalpha() and parte_punto_correo.isalpha() and len(parte_punto_correo) <= 3:
        return True
    else:
        print "El formato del correo es invalido."
        print "=============="
        return False



#Introdcir el correo junto a sus condiciones.
def introducir_correo():
    num_arrobas = 0
    condiciones_correo = False
    while condiciones_correo == False:        
            correo = raw_input("Escriba su correo: ")
            #Cuenta las "@".
            num_arrobas = correo.count("@")
            #Separa el correo.
            correo_separado_arroba = correo.split("@")
            try:
                dominio_correo = correo_separado_arroba[1]
                num_puntos = dominio_correo.count(".")
            except:
                print "El formato del correo es invalido."
                print "=============="
                continue    
            
            #Si hay mas de una "@" hace un PRINT.
            if num_arrobas > 1 or num_arrobas == 0 or num_puntos > 1 or num_puntos == 0:
                print "El formato del correo es invalido."
                print "=============="      
            else:
                condiciones_correo = check_email(correo)
    print "=============="
    return correo



#Introdcir la contrasena junto a sus condiciones.                        
def introducir_contrasena():
    condiciones_contrasena = False
    contrasena = raw_input("Escriba su contrasena: ")
    confirma_contrasena = raw_input("Confirme su contrasena: ")
    while contrasena != confirma_contrasena:
        print "=============="
        print "La constrsena no coincide, por favor vuelva a introducirla."
        print "=============="
        contrasena = raw_input("Escribe tu contrasena: ")
        confirma_contrasena = raw_input("Confirma tu contrasena: ")
    print "=============="
    return contrasena



#Introduce los datos en un diccionario.
def introducir_datos():
    datos_lista[usuario] = "NOMBRE: {0} | APELLIDO: {1} | CORREO: {2} | CONTRASENA: {3}".format(nombre, apellido, correo, contrasena)
    

    
#Confirmar los datos.    
def confirmar_datos():  
    print "Confirme sus datos:"
    print "Usuario:", usuario
    print "Nombre:", nombre
    print "Apellido:", apellido
    print "Correo:", correo
    print "Contrasena:", contrasena
    print "=============="
    while True:
        respuesta = raw_input("Confirme sus datos: (y/n) ")
        if respuesta == "y":
            print "=============="
            #Introduce los datos en una lista.
            print "Datos introducidos en la base de datos."
            introducir_datos()
            condiciones_ciclo = True
            break
        elif respuesta == "n":
            condiciones_ciclo = False
            print "=============="
            break
        else:
            print "=============="
            print "No reconozco esa respuesta, por favor vuelva a introducirla."
            print "=============="



#Guardar los datos en el archivo.
def guardar_datos():
    with open(ruta_txt, "a") as archivo:
        archivo.writelines(("===============\n",
                            "USUARIO: ", usuario,
                            "\nDATOS ASOCIADOS: ", datos_lista[usuario],
                            "\n"))
    informacion = {"info"}
    informacion["info"] = [archivo_json] + [datos_lista]
    
    with open(ruta_json, "w", indent = 2) as archivo_json:
        json.dump(informacion, archivo_json)