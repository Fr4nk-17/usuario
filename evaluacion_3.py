import json

def cargar_usuarios_desde_json(archivo):
    with open(archivo, "r", encoding="utf-8") as file:
        abrir_json = json.load(file)
    return(abrir_json)

def buscar_usuario_por_nombre(lista_usuarios, nombre):
    for estudiante in lista_usuarios:
        if estudiante["nombre"].lower() == nombre:
            return estudiante
    return None

def guardar_usuario_en_txt(usuario, archivo):
    try:
        with open(archivo, 'w') as file:
            for key, value in usuario.items():
                file.write(f"{key}: {value}\n")
        print(f"Se ha guardado la información del usuario en el archivo {archivo}.")
    except IOError:
        print(f"Error al intentar escribir en el archivo {archivo}.")


def main():
    archivo_json = "C:\\python\\usuarios.json"
    lista_usuarios = cargar_usuarios_desde_json(archivo_json)
    
    if not lista_usuarios:
        print("No se pudieron cargar los usuarios. Saliendo del programa.")
        return
    
    nombre_usuario = input("Ingrese el nombre del usuario a buscar: ")
    usuario_encontrado = buscar_usuario_por_nombre(lista_usuarios, nombre_usuario)
    
    if usuario_encontrado:
        print(f"Información del usuario encontrado:\n{usuario_encontrado}")
        archivo_txt = f"{nombre_usuario.lower()}.txt"
        guardar_usuario_en_txt(usuario_encontrado, archivo_txt)
    else:
        print(f"No se encontró al usuario '{nombre_usuario}'.")

if __name__ == "__main__":
    main()









    

    




    