option = 1
empanadas = []
while option != 1:
    print("************empanadas el niche****************")
    print("opcion 1 = ingrese una empanada")
    print("opcion 2 = Mostrar todas las empanadas registradas")
    print("opcion 3 = buscar empanada por 10")
    print("opcion 4 = editar una empanada")
    print("opcion 5 = eliminar una empanada")
    print("Presiona 0 Para salir del Menu")
    option = int (input("escoja opcion: "))
    if(option == 1):
        empanada = {}
        empanada ['id']= int(input("digite el id de la empanada: "))
        empanada ['nombre']= int(input("digite el nombre de la empanada: "))
        empanada ['precio']= int(input("digite el precio de la empanada: "))
        empanada ['popularidad']= int(input("digite la popularidad de la empanada: "))
        empanada ['fechaVen']= int(input("digite la fecha de vencimiento de la empanada: "))
        
        empanadas.append(empanada)
        print("Empanada ingresada...")
    elif(option ==2):
        for empanada in empanadas:
            print(empanada)
    elif(option ==3):
        findEmpanda=int(input("Ingrese el id de la empanada: "))
        for empanada in empanadas:
            if findEmpanda == empanada ["id"]:
                print (f"empanda encontrada... {id}")
            else:
                print("No existe...")
    elif(option == 4):
        findEmpanda=int(input("Ingrese el id de la empanada: "))
        for empanada in empanadas:
            if findEmpanda == empanada ["id"]:
                print (f"El precio de la empanada es: {empanada['precio']}")
                empanada["precio"]=float(input("que precio deseas ingresar: "))
            else:
                print("No existe...")