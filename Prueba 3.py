Valorasientos=("Asiento normal 60000"," Espacio adicional para piernas $80000","No reclina 50000")
pasajeros=[]
Total= asiento_normal + asiento_noreclinable + asiento_grande

def comprarpasaje():
    cant_pasajes=int(input("Cuantos pasajes desea comprar: "))
    #debo de hacer que segun el numero ingresado se vaya peguntando constantemente que tipo de asiento quiere 
    # tiene que tener un limite de 198 asientos, cada vez que se compre un asiento se va calculando la ganancia total y la ganancia por asiento
    for i in range(cant_pasajes):
        input
def ubicaciones():
    pass
    # hacer funcion para mostrar las ubicaciones de los asientos disponibles y de los asientos ocupados 
    
def listapasajeros():
    pass
    #funcion para ver a los pasajeros en un lista segun su rut (el rut debe ser ingresado en la funcion de comprar pasajes) de menor a mayor 

def buscarpasajeros():
    pass
    #funcion para buscar a los pasajeros segun su rut 

def reasignarasientos():
    pass
    #funcion para poder reasignar asientos entre los pasajeros 

def ganancias():
    pass
#debe mostrar las ganancias totales,  de la clase de asientos, e decir si se veden 20 asientos tipo normal que salga en pantalla asiento_normal 20  1.200.000
    
        


while True:
    try:
        print("""
        (1) COMPRAR PASAJES
        (2) MOSTRAR UBICACIONES DISPONIBLES
        (3) VER LISTADO DE PASAJEROS
        (4) BUSCAR PASAJEROS
        (5) REASIGNAR ASIENTOS
        (6) MOSTRAR GANANCIAS TOTALES
        (7) SALIR """)
        
        opcion=int(input("INGRESE OPCION: "))
        if opcion==1:
            comprarpasaje()
        elif opcion==2:
            ubicaciones()
        elif opcion==3:
            listapasajeros()
        elif opcion==4:
            buscarpasajeros()
        elif opcion==5:
            reasignarasientos()
        elif opcion==6:
            ganancias()
        elif opcion==7:
            break
        else:
            print("INGRESE UNA DE LAS OPCIONES EXISTENTES")
    except ValueError:
        print("INGRESE SOLO NUMEROS")