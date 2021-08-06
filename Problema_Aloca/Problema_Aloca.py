################## Instalação do pyomo e do solver para resolver o problema #######################

#!pip install -q pyomo
#!sudo apt install -y -qq glpk-utils

############################### Importando Bibliotecas ###########################################

import pyomo.environ as pyenv
import numpy as np

############################## Dando os Dados de uma Forma Matricial #############################

custos = np.array([[17,18,10,8],[15,16,7,16],[14,13,8,15],[10,15,11,12]])

n_taxis=len(custos[0])
n_clientes=len(custos)

############################ Declarando o Modelo Através de Pyomo ################################

modelo=pyenv.ConcreteModel()

modelo.indices_taxis=pyenv.RangeSet(n_taxis) #retorna [1:4]
modelo.indices_clientes=pyenv.RangeSet(n_clientes) #retorna [1:4]

###### Criando as váriáveis de decisão que serão usadas no método simplex #########################

modelo.variaveis=pyenv.Var(modelo.indices_taxis,modelo.indices_clientes,within = pyenv.NonNegativeReals)

########################## Dando os Dados para o Pyomo ############################################

modelo.custos=pyenv.Param(modelo.indices_taxis,modelo.indices_clientes,initialize=lambda modelo,i,j:custos[i-1][j-1])

########################## Criando a Função Objetivo ##############################################

modelo.objetivo=pyenv.Objective(expr=sum(modelo.variaveis[i,j]*modelo.custos[i,j] for i in modelo.indices_taxis for j in modelo.indices_clientes),sense=pyenv.minimize)

######################### Criando as Restrições ##################################################

# Restrição 1: Cada taxi só receberá um cliente
def rest1(modelo,i):
  return sum(modelo.variaveis[i,j] for j in modelo.indices_clientes) == 1

# Restrição 2: Cada cliente só será atendido por um taxi
def rest2(modelo,j):
  return sum(modelo.variaveis[i,j] for i in modelo.indices_taxis) == 1

######################### Dando as Restrições para o Pyomo ######################################

modelo.rest1= pyenv.Constraint(modelo.indices_taxis, rule=rest1)

modelo.rest2= pyenv.Constraint(modelo.indices_clientes, rule=rest2)

############################# Utilizando  o Solver ###############################################

### Diz qual o solver que será utlizado:

solver = pyenv.SolverFactory('glpk', executable = '/usr/bin/glpsol') 

result_objetivo=solver.solve(modelo,tee=True)

############################ Printando o Resultado ###############################################

lista = list(modelo.variaveis.keys())
a=np.zeros([n_taxis+1,n_clientes+1]) #A será a matriz solução 
for i in lista:
  if modelo.variaveis[i]() != 0:
    a[i]= modelo.variaveis[i]() 
a=a[1:,1:]
print("\n A matriz solução é: \n",a) 

print("Valor da função Objetivo:",modelo.objetivo())

#modelo.display() # Tem essa alternativa de visualização, mas acho ruim 
