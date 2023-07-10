list_asient_plat=[1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 
                38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                55, 56, 58, 59, 60, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 
                72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 
                89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

cant=0
prec=0
cant_gold=0
cant_silver=0
def salir():
        print("""
        Nombre: Benjamin Cortes Parra
        Fecha: 10/07/2023
        """)
s=True
def mostr():
    print(f"""
        Los asientos desponibles son:
        {list_asient_plat}
        """)
def mostr22():
    print(f"""
        Los precios de las entradas son:
        -Platinum, $120.000. (Asientos del 1 al 20)
        -Gold, $80.000. (Asientos del 21 al 50)
        -Silver, $50.000

        
        Los asientos desponibles son:
        {list_asient_plat}
        """)

def elect_asient():
    for i in range (len(list_asient_plat)):
                if i ==int(select)-1 :
                    if list_asient_plat[i]!="X":
                        print("El asiento a sido seleccionado")
                        list_asient_plat[i]="X"
                    else:
                        print("El asiento  NO esta disponible")

#list_asient_plat[i]<=10 and list_asient_plat[i]>=20
def platinum():
    for i in range (len(list_asient_plat)):
        if list_asient_plat[i]=="X":
            if i<=0 and i>=20:
                    cant=cant+1
            elif i<=21 and i>=50:
                cant_gold=cant_gold+1
            elif i<=51 and i>=100:
                cant_silver=cant_silver+1
    print(f"""
    Tipo de Entrada             cantidad            Total
    Platinum $120.000           {cant}              ${cant*120000}
    Gold     $80.000            {cant_gold}         ${cant_gold*80000}
    Silver   $50.000            {cant_silver}       ${cant_silver*50000}
    """)
             
def mostrar9999():
                     print(f"""
                Tipo de Entrada             cantidad            Total
                Platinum $120.000           {cant}              ${cant*120000}
                Gold     $80.000            {cant_gold}         ${cant_gold*80000}
                Silver   $50.000            {cant_silver}       ${cant_silver*50000}
                """)

while s==True:
    print("""
    1.Comprar Entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir
    """)

    op=input("Ingrese una de las opciones a elegir: ")
    match op:
        case "1":
            mostr22()
            select=input("Ingrese su asiento a elegir: ")
            for i in range (len(list_asient_plat)):
                if i ==int(select)-1 :
                    if list_asient_plat[i]!="X":
                        print("El asiento a sido seleccionado")
                        list_asient_plat[i]="X"
                    else:
                        print("El asiento  NO esta disponible")
        case "2":
            mostr()
        case "4":
                for i in range (len(list_asient_plat)):
                    if list_asient_plat[i]=="X":
                        if i<=0 and i>=20:
                            cant=cant+1
                        elif i<=21 and i>=50:
                            cant_gold=cant_gold+1
                        elif i<=51 and i>=100:
                            cant_silver=cant_silver+1
                mostrar9999()
          
        case "5":
            salir()
            break
        case other:
            print("La opcion ingresada no es valida, se le volvera a preguntar")