################### Instalação do Solver e do pyomo ############################

#!pip install -q pyomo

################# Importando as Bibliotecas necessárias ########################

import numpy as np
import pyomo.environ as pyenv

################# Modelando o problema de forma Matricial ######################
''' Desta vez o problema é desbalanceado, então vai ser criada um fabrica fantasma
com custo zero para suprir a Demanda Extra, que, de fato,não será suprida'''
custo=np.array([[600,1300,1600],[1500,1100,700],[0,0,0]])

suprimentos=np.array([130,140,30]) # A fabrica ficticia tem uma capacidade igual a demanda extra
s=len(suprimentos)

demandas=np.array([50,100,150])
d=len(demandas)

################ Modelando o problema através de pyomo #########################

modelo=pyenv.ConcreteModel()

#Criando os indices:
modelo.indices_suprimentos = pyenv.RangeSet(s)
modelo.indices_demandas= pyenv.RangeSet(d)

#Criando as variaveis de decisão:
modelo.var=pyenv.Var(modelo.indices_suprimentos,modelo.indices_demandas,within= pyenv.NonNegativeReals)

#Dando os parâmetros para pyomo:
modelo.custos=pyenv.Param(modelo.indices_suprimentos,modelo.indices_demandas,initialize = lambda  modelo, i, j: custo[i-1][j-1])
modelo.suprimentos=pyenv.Param(modelo.indices_suprimentos,initialize = lambda modelo,i: suprimentos[i-1])
modelo.demandas= pyenv.Param(modelo.indices_demandas,initialize = lambda modelo,j: demandas[j-1])

#Criando uma função objetivo:
modelo.objetivo=pyenv.Objective(expr=sum(modelo.custos[i,j]*modelo.var[i,j] for i in modelo.indices_suprimentos for j in modelo.indices_demandas),sense=pyenv.minimize)

####################### Criando as restrições ##################################

#Restrição Suprimentos:
def rest1(modelo,i):
  return sum(modelo.var[i,j] for j in modelo.indices_demandas)<=modelo.suprimentos[i]
#Restrição Demandas:
def rest2(modelo,j):
  return sum(modelo.var[i,j] for i in modelo.indices_suprimentos)>=modelo.demandas[j]

#################### Dando as Restrições para o pyomo ##########################

#Restrição Suprimentos:
modelo.rest1=pyenv.Constraint(modelo.indices_suprimentos,rule=rest1)

#Restrição Demandas:
modelo.rest2=pyenv.Constraint(modelo.indices_demandas,rule=rest2)

############################ Usando o Solver ###################################

solver = pyenv.SolverFactory('glpk', executable = '/usr/bin/glpsol') 
result_objetivo = solver.solve(modelo, tee = True) 

######################### Printando o resultado ################################

lista = list(modelo.var.keys())
a=np.zeros([s+1,d+1])
for i in lista:
    a[i]= modelo.var[i]() 
a=a[1:,1:]
print("\n A matriz solução é: \n",a)

print("Valor da função Objetivo:",modelo.objetivo())
