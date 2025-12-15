def copiarArchivo(origen, destino):
    with open(origen, "r") as o, open(destino, "w") as d:
        d.write(o.read())

def copiarBinario(origen, destino):
    with open(origen, "rb") as o, open(destino, "wb") as d:
        d.write(o.read())

print("¿que desea hacer?")
print("1. copiar archivo de texto")
print("2. copiar archivo binario")

opcion = input("ingrese una opcion: ")

try:
    archivoOrigen = input("ingrese el nombre del archivo de origen: ")
    archivoDestino = input("ingrese el nombre del archivo de destino: ")

    if opcion == "1":
        copiarArchivo(archivoOrigen, archivoDestino)
        print("archivo de texto copiado correctamente")
    elif opcion == "2":
        copiarBinario(archivoOrigen, archivoDestino)
        print("archivo binario copiado correctamente")
    else:
        print("Opción inválida")

except FileNotFoundError:
    print("Error: el archivo no existe")
except PermissionError:
    print("Error: permisos insuficientes")
