# Solução 

## Construção do Modelo 

O modelo de Programação Linear será dado por:

- Função Objetivo:
  - max( Lucro = 1,5.xq + 2.xd + 1,2.xr )
 
- Restrições:
  - 3.xq + 2.xd + xr <= 5760 (restrição de tempo --> 12 empregados trabalhando 8 [horas/dia] = 5760 [minutos])
  
  - 10.xq + 6.xd < = 8000 (restrição de material --> Litros de Leite)

  - xq >= 3.xd (restrição de demanda --> Dados no enunciado do Problema)
  - xd <= 200 (restrição de demanda --> Dados no enunciado do Problema)
  - xr <= xq/3 (restrição de demanda --> Dados no enunciado do Problema)

- Legenda:
  - xq = quantidade de queijo 
   -xd = quantidade de doce 
   
 ## Explicação e Resolução do Problema
A variável “xr”(quantidade de ricota) não foi utilizada no algoritmo de solução, pois, como a mesma é um subproduto da quantidade de queijo( dado fornecido no enunciado ), ela será substituída pela relação desta com “xq”(quantidade de queijo).Tal como mostra o exemplo abaixo:

3.xq + 2.xd + xr = 5760 (Restrição de minutos trabalhados disponíveis)
Como xr = xq/3
3.xq + 2.xd + xr/3 = 5760
(10/3).xq + 2.xd = 5760 
