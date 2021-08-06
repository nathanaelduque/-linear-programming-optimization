# Solução

## Construindo o Modelo 

O modelo de Programação Linear será dado por:

- Função Objetivo:
  - min( tempo = 17.x11 + 18.x12 + 10.x13 + 8.x14 + 15.x21 + 16.x22 + 7.x23 + 16.x24 + 14.x31 + 13.x32 + 8.x33 + 15.x34 + 10.x41 + 15.x42 + 11.x43 + 12.x44 )
 
- Restrições:
  -  Σ(xij) = 1 (restrição de atribuição --> somente um taxi deverá ser atribuido para cada cliente e somente um cliente para cada táxi )
  
  - xij = [0,1] (restrição de variável binária --> 0:não atenderá,1:atenderá)

- Legenda:
  - xij = Taxi i atende cliente j 
   
 ## Explicação e Resolução do Problema
 
Para modelar tal problema, usa-se uma matriz unimodular, isso faz com que somente um cliente seja atendido por somente um táxi e que um táxi atenda somente um cliente.
    
A partir dessa matriz, da biblioteca Pyomo e do solver GLPK, resolve-se esse problema de alocação dinâmica,e descobre-se que a matriz solução,que designa cada carro a somente uma corrida será como mostrado abaixo, o tempo mínimo total será de 38 minutos.

<div align="center">

x| Cliente 01 | Cliente 02 | Cliente 03 | Cliente 04
:------------: | :-------------: | :-------------: | :-------------: |  :-------------: 
**Taxista 1** | 0 | 0 | 0 | 1
**Taxista 2** | 0 | 0 | 1 | 0
**Taxista 3** | 0 | 1 | 0 | 0 
**Taxista 4** | 1 | 0 | 0 | 0 
 
</div>
