## Atividade Prática do Curso Introdução ao Data Science

# Análise Exploratória de Dados - Titanic :ship:

O presente projeto é uma análise da lista de pessoas passageiras do navio Titanic em sua famosa viagem inaugural. O objetivo é realizar uma análise exploratória dos dados e em particular analisar alguns fatores relacionados à probabiblidade de sobrevivência, como parte da atividade prática do curso de Introdução ao Data Science oferecido pelo Lab365 no contexto do programa SCTEC.

## :books: Bibliotecas utilizadas

Este projeto foi desenvolvido utilizando um ambiente virtual para controle das bibliotecas. As bibliotecas utilizadas foram:
- Pandas: para manipulação e análise do dataset.
- Matplotlib e Seaborn: para visualização dos dados em gráficos.

## :open_file_folder: Preparação dos dados

Foi verificada a possibilidade de linhas duplicadas no conjunto de dados para remoção caso necessário.

Foi feita também uma verificação de valores nulos. Apenas as colunas _Age_, _Cabin_ e _Embarked_ apresentam valores nulos. A coluna _Age_ possui 177, a coluna _Cabin_ possui 687 e a coluna _Embarked_ possui 2 valores nulos. Como nenhuma dessas colunas foi utilizada na presente análise, os respectivos registros foram mantidos no dataset.

## :bar_chart: Relatório de Análise

A análise dos dados do Titanic revelou informações sobre a relação entre as características das pessoas passageiras e suas taxas de sobrevivência. A seguir, estão os principais pontos observados:

### Gênero e sobrevivência

O navio tinha 891 pessoas passageiras, das quais 342 sobreviveram e 549 não. A taxa de sobrevivência geral foi de aproximadamente 38%.

Entre as pessoas passageiras, 577 (65%) eram homens e 314 (35%) eram mulheres.

A taxa de sobrevivência para as mulheres foi significativamente maior do que para os homens, com aproximadamente 74% das mulheres retornando vivas, em comparação com apenas 19% dos homens.

Os gráficos abaixo permitem compararmos a proporção de homens e mulheres no navio com a proporção de homens e mulheres no grupo de sobreviventes, o que corrobora aquela ideia de "mulheres e crianças primeiro" popularizada pela ficção:

<p align="center">
<img src="images/Figure_1.png" alt="Proporção de Homens e Mulheres" width="45%" >
<img src="images/Figure_2.png" alt="Proporção de Homens e Mulheres Sobreviventes" width="45%" >
</p>

### Classe no navio e preço da passagem

Foi observada a relação entre a classe no navio e a tarifa paga pela pessoa passageira através de um gráfico de violino. O Titanic tinha três classes: primeira, segunda e terceira classe. Em média, o preço do bilhete pago pelas pessoas viajantes da primeira classe foi mais alta do que o pago pelas pessoas viajantes da segunda e terceira classes: a tarifa média da primeira classe foi de cerca 84 dólares, enquanto a da segunda classe foi de 20 dólares e a da terceira classe de 13 dólares.

<p align="center">
<img src="images/Figure_3.png" alt="Tarifas por Classe no Navio">
</p>

Foi calculada a medida de correlação entre a classe no navio e o preço da passagem, com um coeficiente calculado em **-0.55**, indicando uma correlação negativa moderada. Isso significa que as pessoas passageiras de classes mais altas (primeira classe) pagaram tarifas maiores do que aquelas de classes mais baixas (segunda e terceira classes) — a correlação é negativa porque à medida que a classe no navio aumenta (1 → 2 → 3), a tarifa diminui. Como a tarifa é uma variável numérica contínua, foi utilizado o método Pearson para este cálculo de correlação.

A motivação aqui foi de utilizar **a classe no navio como um proxy para o status socioeconômico** dos passageiros diante da suspeita que a classe social teve impacto na sobrevivência da pessoa passageira, verificada a seguir.

### Classe social e sobrevivência

A análise da relação entre a classe social e a sobrevivência revelou que as pessoas passageiras da primeira classe tiveram uma taxa de sobrevivência realmente maior do que as da segunda e terceira classes. Aproximadamente 63% das pessoas que estavam na primeira classe sobreviveram, em comparação com cerca de 47% das pessoas na segunda classe e apenas 24% das na terceira classe, como mostrado no gráfico de barras abaixo. Esses resultados apontam que a classe social teve impacto na probabilidade de sobrevivência das pessoas a bordo do Titanic.

<p align="center">
<img src="images/Figure_4.png" alt="Taxa de Sobrevivência por Classe no Navio">
</p>

Foi calculado o coeficiente de correlação entre a classe no navio e a sobrevivência, que resultou em um valor de aproximadamente **-0.34**, indicando uma correlação negativa moderada. Isso sugere que pessoas passageiras de classes mais altas (primeira classe) tinham uma probabilidade maior de sobreviver do que aquelas de classes mais baixas (segunda e terceira classes). (Mais uma vez, a correlação é negativa porque à medida que a classe no navio aumenta (1 → 2 → 3, ficando menos luxuosas), a taxa de sobrevivência diminui.)

Foi utilizado o método Spearman para este cálculo de correlação por ser mais adequado para avaliar a relação entre variáveis ordinais, como a classe no navio. Embora a classe no navio possa ser expressa numericamente (1, 2 e 3), aproveitei a ausência de uma variável numérica contínua para enfatizar sua dimensão ordinal, uma vez que as classes estão ordenadas (a primeira classe sendo melhor do que a segunda, que é melhor do que a terceira).

### Considerações finais

A análise dos dados do Titanic revela que o gênero e a classe social tiveram um impacto significativo na sobrevivência das pessoas passageiras. As mulheres tiveram uma taxa de sobrevivência muito maior do que os homens, assim como as pessoas passageiras da primeira classe tiveram uma taxa de sobrevivência significativamente maior do que as da segunda e terceira classes, sugerindo que as pessoas de classes sociais mais altas tiveram acesso a melhores recursos e oportunidades de sobrevivência durante o desastre.

[Link no GitHub](https://github.com/FelipeQue/SCTEC-desafio-opcional-dados)