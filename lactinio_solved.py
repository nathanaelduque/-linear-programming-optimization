################## Instalando o Solver e o Pyomo ###############################

#sudo apt install coinor-cbc
#!pip install pyomo

############### Importando as Bibliotecas necessárias ##########################

import pyomo.environ as pyo
import numpy as np

############ Dando os Dados do Problema de Forma Matricial #####################

#Lucro:
L= np.array([1.9,2])

#Produção diária de leite:
leite_t=np.array([8000])

#Leite exigido de cada produto:
leite_p=np.array([10,6])

#Total de minutos disponíveis:
h_t= np.array([5760])

#horas exigidas de cada produto:
h_p= np.array([10/3,2])

################# Construindo o modelo com a Pyomo #############################

modelo= pyo.ConcreteModel()

#Número de variáveis de decisão:
n=len(L) 

#Construindo as variáveis de decisão:
modelo.var=pyo.Var([i for i in range (n)],domain=pyo.NonNegativeReals)

#Construindo a função objetivo:
expr=sum(L[i]*modelo.var[i] for i in range (n))
modelo.obj=pyo.Objective(expr=expr, sense=pyo.maximize)

#Construindo o conjunto de restrições:

#Restrições por hr trabalhada:
modelo.rest1=pyo.Constraint(expr=sum(h_p[i]*modelo.var[i] for i in range(n))<=h_t[0])

#Restrição da Quantidade de Doce de Leite:
modelo.rest2=pyo.Constraint(expr=modelo.var[1]<=200)

#Restrição xq>=3*xd:
modelo.rest3=pyo.Constraint(expr=modelo.var[0]>=3*modelo.var[1])

#Restrição quantidade de leite:
modelo.rest4=pyo.Constraint(expr=sum(leite_p[i]*modelo.var[i] for i in range(n))<=leite_t[0])

###################### Resolvendo através do solver ############################

solver = pyo.SolverFactory("cbc", executable="/usr/bin/cbc")
results = solver.solve(modelo)

######################### Printando os Resultados ###############################

a=[]
for i in range (0,n):
    a.append( modelo.var[i]() )
print("O lucro ótimo é",  modelo.obj.expr())
print("Quantidade de queijo produzida: ",a[0])
print("Quantidade de ricota produzida:",a[0]/3)
print("Quantidade de doce de leite:",a[1])