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

    def setVecinos(self, vecinos):
        self.vecinos=vecinos

    def setDominio(self, dominio):
        self.dominio=dominio



# def fordward_checking(Xi,v):
#     Xi.dominio = [v]
#     vecinos=neighbors(Xi)
#     for Xe in neighbors(Xi):


# def mrv(X):
#     ordered_variables = pqueue();

# def backtrack(assignment, csp):
#     if (assignment is complete):
#         return assignment
#     var = select_unassigned_variable(csp)
#     for value in order_domain_values(var, )

def main():
    juslan=Expositor("Juslan","seguInf")
    pablo=Expositor("Pablo","ingSoft")
    jorge=Expositor("Jorge","intArt")
    pedro=Expositor("Pedro","seguInf")

    dominio=[juslan,pablo,jorge,pedro]
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
    horarios=[hora1,hora2,hora3,hora4,hora5,hora6,hora7,hora8,hora9,hora10,hora11,hora12,hora13,hora14,hora15,hora16]
    HorariosDia=[horarios,horarios,horarios,horarios,horarios] #Lunes==HorariosDia[0]....Viernes==HorariosDia[4]


    # if dominio[0].area==dominio[2].area:
    #     print("Las areas son iguales")
    # else:
    #     print("Las areas son DIFERENTES")



# • Seguridad Informatica  == seguInf
# • Ingenierıa de Software == ingSoft
# • Inteligencia Artificial == intArt
if __name__ == '__main__':
    main()

