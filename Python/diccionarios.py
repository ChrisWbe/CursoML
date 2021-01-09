paciente1 = {"nombre":"Juan", "edad":32, "fuma":False, "peso":70.5, 666:False} #Es posible que una llave sea un indice numerico
paciente2 = {"nombre":"Juan", "edad":32, "fuma":False, "peso":70.5, 666:True}
paciente3 = {"nombre":"Juan", "edad":32, "fuma":False, "peso":70.5, 666:True}
pacientes = [paciente1,paciente2,paciente3]
print(paciente1)
print(type(paciente1))

print(paciente1['nombre'])
print(paciente1.get('fuma'))

paciente1.pop("edad")
print(paciente1)

paciente1.update({"peso":80.9}) #Ambos actualizan
print(paciente1)
paciente1['peso']=80.5
print(paciente1)

print("peso" in paciente1)

print(pacientes)
for paciente in pacientes:
    for clave,valor in paciente.items():
        print("Clave -> ",clave," \t|\t Valor -> ",valor)
    print("*******************************************")


