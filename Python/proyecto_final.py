def menu():
    print("\t\t1 - Cargar paciente")
    print("\t\t2 - Buscar paciente por nombre")
    print("\t\t3 - Listar pacientes")
    print("\t\t4 - Salir")
    return int(input("Ingresa tu seleccion -> "))

def welcome():
    print("*************************")
    print("* Mensaje de bienvenida *")
    print("*************************")

def loadData(pacientes=list()):
    p = dict()
    p["nombre"]=input("Ingrese el nombre -> ")
    p["edad"]=input("Ingrese la edad -> ")
    p["peso"]=input("Ingrese el peso -> ")
    pacientes.append(p)

def findXName(pacientes=list(), name=str()):
    for paciente in pacientes:
        if(paciente['nombre']==name):
            print(paciente)

    

def printData(pacientes=list()):
    for paciente in pacientes:
        print(paciente)


running = True
pacientes = list()
welcome()
while(running):
    
    selection = menu()
    if selection == 1:
        loadData(pacientes)
        print(pacientes)
    elif selection == 2:
        name = input("Ingrese el nombre del paciente -> ")
        findXName(pacientes, name)
    elif selection == 3:
        printData(pacientes)
    elif selection == 4:
        running = False
    else:
        print("******** Valor Inválido ********")
    


