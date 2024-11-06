import json 

#esta sera la funcion que va a leeer y cargar los datos del Acces.json a cualquier funcion del sistema
def cargar_datos():
    with open("data\Acces.json", "r") as Acces:
        #ahora aqui usamos .load para que el json cargue el Acces a python para su lectura y posterior modificacion
        datos_del_json = json.load(Acces)
    #esto devolvera el archivo del acces ya cargado
    return datos_del_json

#y esta sera la funcion que se va encargar de escribir en la estructura del json los cambios de las funciones y guarde los datos en el json
def guardar_datos(datos_del_json):
    #Aqui puse que si datos_del_json no es un diccionario no lo va a poder guardar, esto es para evitar errores
    #por si acaso alguien quiere crear una funcion y olvide que json solo maneja diccionarios
    if type(datos_del_json) != dict:
        print("Los datos deben ser un diccionario")
        return False
    #si no se cumple esa condicion entonces simplemente guardara los datos en el archivo de Acces.json
    with open("data\Acces.json", "w") as Acces:
        #el .dump nos dejara reescribir el JSON desde el python
        json.dump(datos_del_json, Acces, indent=4)
    return True


 