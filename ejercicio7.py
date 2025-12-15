def copiarArchivo(origen, destino):
    with open(origen, "r") as o, open(destino, "w") as d:
        d.write(o.read())

def copiarBinario(origen, destino):
    with open(origen, "rb") as o, open(destino, "wb") as d:
        d.write(o.read())

print("¿Qué desea hacer?")
print("1. Copiar archivo de texto")
print("2. Copiar archivo binario")

opcion = input("Ingrese la opción: ")

try:
    archivoOrigen = input("Ingrese el nombre del archivo de origen: ")
    archivoDestino = input("Ingrese el nombre del archivo de destino: ")

    if opcion == "1":
        copiarArchivo(archivoOrigen, archivoDestino)
        print("Archivo de texto copiado correctamente")
    elif opcion == "2":
        copiarBinario(archivoOrigen, archivoDestino)
        print("Archivo binario copiado correctamente")
    else:
        print("Opción inválida")

except FileNotFoundError:
    print("Error: el archivo no existe")
except PermissionError:
    print("Error: permisos insuficientes")
