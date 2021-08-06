# Solução

## Construção do Modelo 

O modelo de Programação Linear será dado por:

- Função Objetivo:
  - min( Gastos = 600.x11 + 1300.x12 + 1600.x13 + 1500.x21 + 1100.x22 + 700.x23 )  
 
- Restrições:
  - x11 + x12 + x13 <= 130 (restrição de suprimento da Fábrica 01)
  
  - x21 + x22 + x23 <= 140 (restrição de suprimento da Fábrica 02)

  - x11 + x21 >= 50 (restrição de demanda da CD 01)
  - x12 + x22 >= 100 (restrição de demanda)
  - x13 + x23 >= 120 (restrição de demanda)

- Legenda:
  - xij = quantidade transportada desde a Fábrica i até o centro de distribuição j

## Explicação e Resolução do Problema 

Nesse tópico foi resolvido um exemplo clássico do Problema do Transporte balanceado,onde tem-se um determinado número de centros de distribuição e um determinado número de fábricas, nesse caso,por ser um problema balanceado, a demanda total é igual a produção total.

Como já foi fornecida a matriz de custos, ao invés da matriz de distâncias(que é o que normalmente é fornecido), a mesma foi utilizada dentro do algoritmo em python.O problema foi modelado primeiramente em uma forma matricial, e depois, foi modelado através da biblioteca pyomo, e resolvido com o auxílio do solver glkp.No final tem-se mostrado a matriz solução que irá resultar em um custo mínimo de transporte.A matriz encontrada é apresentada abaixo.
**O custo final é igual a: R$ 240000,00**


