#1
arreglo_nombre = []
#2
arreglo_rut = []
#3
arreglo_peso_paquete = []
#4
arreglo_ciudad = []
#5
arreglo_precios = []
#6
arreglo_tipo_paquete = []

def grabar():
    while True:
        try:
            rut = str(input("INGRESE SU RUT:\n"))
            if rut[-2] == "-":
                arreglo_rut.append(rut.upper())
                print(arreglo_rut)
            else:
                print("POR FAVOR INGRESE UN GUIÓN '-' EN EL PENÚLTIMO LUGAR")

            nombre = str (input("INGRESE SU NOMBRE:\n"))
            if len(nombre) >=2 and len(nombre) <= 30:
                arreglo_nombre.append(nombre.upper())
                print(arreglo_nombre)
            else:
                print("POR FAVOR INGRESE UN NOMBRE CON 2 O MÁS CARÁCTERES O CON 30 O MENOS")
            
            ciudad = input("INGRESE LA CIUDAD DE DESTINO:\n")
            if len(ciudad) >= 3:
                arreglo_ciudad.append(ciudad.upper())
            else:
                print("INGRESE UNA CIUDAD CON MÁS DE TRES LETRAS")
            
            tipo_paquete = input("INDIQUE EL TIPO DE PAQUETE:\n1.- SOBRE\n2.- PAQUETE")
            if tipo_paquete == 1:
                arreglo_tipo_paquete.append("SOBRE")
            elif tipo_paquete == 2:
                arreglo_tipo_paquete.append("PAQUETE")

            peso = float(input("INGRESE EL PESO EN KG:\n"))
            if peso >= 0.1:
                arreglo_peso_paquete.append(peso)
            else:
                print("INGRESE UN PESO MAYOR O IGUAL A 0.1 GR")
            
            precio = float(input("INGRESE EL PRECIO:\n"))
            if precio >= 2000:
                arreglo_precios.append(precio)
            else:
                print("INGRESE UN PRECIO MAYOR O IGUAL A $2.000")
            
            continuar = input("Desea continuar?")
            if continuar == "s":
                menu()

        except:
            print("INGRESE LOS DATOS DE MANERA CORRECTA")
def buscar():
    input("INGRESE EL RUT A BUSCAR")
    print("SORRY PROFE NO ME ACUERDO COMO BUSCAR CON UN INPUT ESPECÍFICO")
    
        
def listar_encomiendas():
    if arreglo_nombre.index == 0:
        for i in arreglo_rut:
            for j in arreglo_nombre:
                for h in arreglo_ciudad:
                    for y in arreglo_precios:
                        for k in arreglo_peso_paquete:
                            for u in arreglo_tipo_paquete:
                                print(arreglo_rut, " : ", arreglo_nombre, " : ", arreglo_ciudad, " : ", arreglo_precios, " : ", arreglo_peso_paquete, " : " , arreglo_tipo_paquete)
                                break

def menu():
    print("Menu Caracol Express".center(30))
    opc = int (input("""1.- Grabar
2.- Buscar
3.- Listar Encomiendas
4.- Salir
Por favor seleccione una opción:\n"""))
    if opc == 1:
        grabar()
    elif opc == 2:
        buscar()
    elif opc == 3:
        listar_encomiendas()
    elif opc == 4:
        print("ADIÓS, ESPERAMOS VUELVAS PRONTO")
        return
menu()

