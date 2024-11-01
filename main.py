from random import *

#Instanciamos nuestras variables locales - Para juntarlas las convertidos en 
productos = ["Laptop", "Smartphone", "Tablet", "Auriculares", "Monitor"]
precios = [1000, 500, 300, 100, 700]

orden = []

#Creamos el catalogo y lo instanciamos como un diccionario
catalogo = dict(zip(productos, precios))

def mostrar_menu():
    """
    Mostramos el menú para que el cliente interactue con él, lo traemos directamente con nuestro
    catalogo

    Parámetros:
    - N/A

    Retorna:
    - None
    """

    print("--- BIENVENIDO A NUESTRO SISTEMA DE COMPRAS - OMNI.PRO ---")
    print("\n A CONTINUACIÓN SELECCIONE EL PRODUCTO QUE QUIERE INCLUIR EN SU CARRITO \n")
    cont = 1
    for producto,precio in catalogo.items():
        print(f"{cont}. {producto} su precio por unidad: {precio}")
        cont += 1
    print("0. Terminar compra")

def seleccionar_productos():
    """
    Función que se encarga del funcionamiento correcto del menú, además
    almacena correctamente todos los productos que ingresa el cliente (acepta repetidos)

    Parámetros:
    - parametro1: n/a

    Retorna:
    - tipo_de_retorno: None
    """

    mostrar_menu()
    while True:
        try:
            opcion = int(input("\n Indica el número de la opción: "))
            if opcion >= 1 and opcion <= 5:
                seleccion = list(catalogo.items())
                orden.append(seleccion[opcion - 1])
                print(f"Has añadido al carrito: {seleccion[opcion - 1]}")
            elif opcion == 0:
                print("\n--- GRACIAS POR UTILIZAR NUESTROS SERVICIOS ;) \n")
                break
            else:
                print("Número no dentro de la opción disponible :(")
        except ValueError:
            print("¡¡¡ ERROR - SELECCION EQUIVOCADO ¡¡¡")

def mostrar_factura():
    """
    Muestra en su totalidad la orden del cliente producto por producto
    en orden en que los fue almacenando el cliente en la variable (orden)

    Parámetros:
    - parametro1: N/A

    Retorna:
    - None
    """

    #Generamos nuestro resumen con el list comprehension
    resumen = [f"{producto} - Precio: {precio}" for producto,precio in orden]

    #Generamos el número de seguimiento con randint (para obtener entero) y list comprehension

    id = str([randint(0,9) for i in range(0,8)]).replace(",",'')
    print(f"ID de Compra: {id}")

    print("-"*30)
    for item in resumen:
        print(item)
        print("-" * 30)

    print(f"El total de su compra es: {precio(len(orden), sum(precio for _, precio in orden))}")


def precio(cant, total) -> int:

    """
    Se encarga de retornar el total del precio de la orden

    Parámetros:
    - cant: la cantidad de productos que tiene
    - total: la suma general de toda la orden 

    Retorna:
    - tipo_de_retorno: Retorna el total, con o sin descuento, dependiendo de si cumple la condición
    """

    if cant >= 5:
        print("OBTUVISTE EL 10% POR TU COMPRA")
        print("-" * 30)
        return total - (total*0.10) 
    if cant >= 3 and cant < 5:
        print("OBTUVISTE EL 05% POR TU COMPRA")
        print("-" * 30)
        return total - (total*0.05)
    else:
        return total

    
def main():
    seleccionar_productos()
    mostrar_factura()

if __name__ == "__main__":
        main()


            
