#  Creamos el diccionario de los productos
catalogo = {
    "Linea Blanca": {
        "LB001": ["Nevera", 2500000],
        "LB002": ["Lavadora", 1800000]
    },
    "Pequeños Electrodomésticos": {
        "PE001": ["Licuadora", 120000],
        "PE002": ["Plancha", 90000]
    },
    "Entretenimiento": {
        "EN001": ["Televisor", 950000],
        "EN002": ["Teatro en casa", 800000]
    },
    "Aires Acondicionados": {
        "AC001": ["Aire 9000 BTU", 1300000],
        "AC002": ["Aire 12000 BTU", 1500000]
    }
}
# Clase Factura
class Factura:
    def __init__(self, cliente):
        self.cliente = cliente    # nombre del cliente
        self.items = []          #lista donde se guarddan los productos que comprsmo
        self.subtotal = 0    #precio sin iva
        self.iva = 0           #iva
        self.total = 0          #precio total con iva
    #creamos una funcion que agregue los productos a la factura
    def agregar_item(self, nombre, precio, cantidad):
        subtotal_item = precio * cantidad      #Hacemos la operacion para sacar el subtotal del producto
        self.items.append([nombre, precio, cantidad, subtotal_item]) #hacemos que el producto se agrege ala liata
    #creamos una funcion que calcule los totales
    def calcular_totales(self):
        self.subtotal = 0  #inicializamos el subtotal en 0
        for item in self.items: #suma de todos los productos
            self.subtotal += item[3]
        self.iva = self.subtotal * 0.19  #calculamos el iva
        self.total = self.subtotal + self.iva
    def mostrar_factura(self):  #hacemos una funcion que muestre la factura
        print(" FACTURA ELECTRÓNICA ")
        print("Cliente:", self.cliente)
        print("Producto\tPrecio\tCant.\tSubtotal")
        for i in self.items:  #recorre todos los productos y los imprime
            print(i[0], "\t", i[1], "\t", i[2], "\t", i[3])
        print("Subtotal:", self.subtotal)  #muestra los totales
        print("IVA (19%):", self.iva)
        print("TOTAL:", self.total)
    def guardar_factura(self): #creamos una funcion que guarde la factura
        nombre_archivo = "factura_" + self.cliente + ".txt" #nombre del archivo es el nombre del cliente
        archivo = open(nombre_archivo, "w") #crea o edita la factura
        archivo.write("FACTURA ELECTRÓNICA\n")
        archivo.write("Cliente: " + self.cliente + "\n\n")
        archivo.write("Producto\tPrecio\tCant.\tSubtotal\n")
        for i in self.items: #escribe tdos los productos enel archivio
            archivo.write(i[0] + "\t" + str(i[1]) + "\t" + str(i[2]) + "\t" + str(i[3]) + "\n")
        archivo.write("\nSubtotal: " + str(self.subtotal))
        archivo.write("\nIVA (19%): " + str(self.iva))
        archivo.write("\nTOTAL: " + str(self.total))
        archivo.close()
        print("Factura guardada en el archivo:", nombre_archivo)
# Creamos una funcion para mostrar el catalogo de productos
def mostrar_catalogo():
    print("\nCATÁLOGO DE PRODUCTOS:")
    for categoria in catalogo:
        print("\n--", categoria, "--")
        for codigo, datos in catalogo[categoria].items():
            print(codigo, "-", datos[0], "-", datos[1]) #imprime el codigo nombre y precio del producto
def buscar_producto(codigo): #creamos una funcion para buscar el producto por su codigo
    for categoria in catalogo:
        if codigo in catalogo[categoria]:               #recorre las categorias y retorno el producto si lo encuentra
            return catalogo[categoria][codigo]
    return None
# nueva funcion para mostrar las facturas guardadas
import os
def mostrar_facturas_guardadas():
    print("\nFACTURAS GUARDADAS:")
    archivos = [f for f in os.listdir() if f.startswith("factura_") and f.endswith(".txt")]
    if len(archivos) == 0:
        print("No hay facturas guardadas.")
    else:
        for i, archivo in enumerate(archivos, start=1):
            print(i, "-", archivo)
        opcion = int(input("\nIngrese el número de la factura que desea ver: "))
        if 1 <= opcion <= len(archivos):
            nombre_archivo = archivos[opcion - 1]
            print("\nContenido de", nombre_archivo, ":\n")
            with open(nombre_archivo, "r") as f:
                print(f.read())
        else:
            print("Opción no válida.")
# Programa principal
def main():
    print("SISTEMA DE FACTURACIÓN ELECTRÓNICA\n")
    cliente = input("Ingrese el nombre del cliente: ")
    factura = Factura(cliente)
    while True:  #creamos un bucle para agregar productos
        print("\n--- MENÚ ---")
        print("1. Crear nueva factura")
        print("2. Ver facturas guardadas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                mostrar_catalogo()
                codigo = input("\nIngrese el código del producto (o 'fin' para terminar): ")
                if codigo.lower() == "fin":  #si escribe fin se acaba el ciclo
                    break
                producto = buscar_producto(codigo) #busca el rpoducto en el catalogo
                if producto is None:
                    print("Código no válido. Intente de nuevo.")
                else:  #si el producto existe pide la anctidad y lo agrega ala facturs
                    cantidad = int(input("Cantidad: "))
                    nombre = producto[0]
                    precio = producto[1]
                    factura.agregar_item(nombre, precio, cantidad)
                    print("Producto agregado con éxito.")
            factura.calcular_totales()
            factura.mostrar_factura()
            factura.guardar_factura()

        elif opcion == "2":
            mostrar_facturas_guardadas()

        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")
main()
