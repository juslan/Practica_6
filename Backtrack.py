# • Seguridad Informatica  == seguInf
# • Ingenierıa de Software == ingSoft
# • Inteligencia Artificial == intArt

class Expositor:
    def __init__(self,name,area):
        self.nombre=name
        self.area=area
        
    def setArea(self, area):
        self.area=area

class Variable:
    def __init__(self,hora,dominio):
        self.horario=hora
        self.vecinos=[]
        self.dominio=dominio
        self.asignacion=""

    def setVecinos(self, vecinos):
        self.vecinos=vecinos

    def setDominio(self, dominio):
        self.dominio=dominio

    def setasignacion(self, asignacion):
        self.asignacion=asignacion

def neighbors(Xi):
    vecinos=[]
    for aux in Xi.vecinos:
        if(aux.asignacion==""):
            vecinos.append(aux)
    return vecinos

def fordward_checking(Xi,v):
    Xi.dominio = [v]
    vecinos=neighbors(Xi)
    borrar = None
    for Xe in neighbors(Xi):
        for i in Xe.dominio:
            if i.nombre==v[0].nombre and i.area==v[0].area:
                borrar=Xe
                break
            break
        if(borrar!=None):
            Xe.remove(borrar)
    
# def mrv(X):
#     ordered_variables = pqueue();

# def backtrack(assignment, csp):
#     if (assignment is complete):
#         return assignment
#     var = select_unassigned_variable(csp)
#     for value in order_domain_values(var, )

def main():
    #exhibitor
    juslan=Expositor("Juslan","seguInf")
    pablo=Expositor("Pablo","ingSoft")
    pablo2=Expositor("Pablo","intArt")
    jorge=Expositor("Jorge","intArt")
    pedro=Expositor("Pedro","seguInf")

    dominio=[juslan,pablo,jorge,pedro]
    #presentations hours
    hora1=Variable("9 seguInf",dominio)
    hora2=Variable("9 ingSoft",dominio)
    hora3=Variable("9 intArt",dominio)
    hora4=Variable("10 seguInf",dominio)
    hora5=Variable("10 ingSoft",dominio)
    hora6=Variable("10 intArt",dominio)
    hora7=Variable("11 seguInf",dominio)
    hora8=Variable("11 ingSoft",dominio)
    hora9=Variable("11 intArt",dominio)
    hora10=Variable("15 seguInf",dominio)
    hora11=Variable("15 ingSoft",dominio)
    hora12=Variable("15 intArt",dominio)
    hora13=Variable("16 seguInf",dominio)
    hora14=Variable("16 ingSoft",dominio)
    hora15=Variable("16 intArt",dominio)
    hora16=Variable("17 seguInf",dominio)
    hora17=Variable("17 ingSoft",dominio)
    hora18=Variable("17 intArt",dominio)
    #setting neighbors
    hora1.setVecinos([hora2,hora3,hora4])
    hora2.setVecinos([hora1,hora3,hora5])
    hora3.setVecinos([hora1,hora2,hora6])
    hora4.setVecinos([hora1,hora5,hora6,hora7])
    hora5.setVecinos([hora2,hora4,hora6,hora8])
    hora6.setVecinos([hora3,hora4,hora5,hora9])
    hora7.setVecinos([hora4,hora8,hora9,hora10])
    hora8.setVecinos([hora5,hora7,hora9,hora11])
    hora9.setVecinos([hora6,hora7,hora8,hora12])
    hora10.setVecinos([hora7,hora11,hora12,hora13])
    hora11.setVecinos([hora8,hora10,hora12,hora14])
    hora12.setVecinos([hora9,hora10,hora11,hora15])
    hora13.setVecinos([hora10,hora14,hora15,hora16])
    hora14.setVecinos([hora11,hora13,hora15,hora17])
    hora15.setVecinos([hora12,hora13,hora14,hora18])
    hora16.setVecinos([hora13,hora17,hora18])
    hora17.setVecinos([hora14,hora16,hora18])
    hora18.setVecinos([hora15,hora16,hora17])
    #Making one day of presentations with hours
    horarios=[hora1,hora2,hora3,hora4,hora5,hora6,hora7,hora8,hora9,hora10,hora11,hora12,hora13,hora14,hora15,hora16]
    #All the variables of 5 days
    variables=[horarios,horarios,horarios,horarios,horarios] #Lunes==HorariosDia[0]....Viernes==HorariosDia[4]
    lista=neighbors(variables[0][0])
    # print(lista)
    # for aux in variables[0][2].vecinos:
    #     print(len(aux.dominio))

    # print(variables[0][0].horario)

    # if dominio[0].area==dominio[2].area:
    #     print("Las areas son iguales")
    # else:
    #     print("Las areas son DIFERENTES")



# • Seguridad Informatica  == seguInf
# • Ingenierıa de Software == ingSoft
# • Inteligencia Artificial == intArt
if __name__ == '__main__':
    main()





