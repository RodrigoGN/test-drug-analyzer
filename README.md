# Drug Analyzer

## Introduction

Você é membro de uma equipe de programação de biotecnologia responsável por criar um sistema para técnicos de laboratório, que os auxiliará na análise de medicamentos.

Seu objetivo é criar o aplicativo que permitirá que eles insiram suas descobertas no sistema, forneçam uma análise significativa e verifiquem a exatidão dos dados que enviaram.

## Prerequisites

Para concluir esta tarefa, use`Python 3`.

### Part 1

Seu objetivo nesta parte é implementar a classe `app.drug_analyzer.DrugAnalyzer`. Será responsável por analisar dados como os dados apresentados abaixo:
```
+-----------+-------------+------------------+-------------+
|   pill_id | pill_weight | active_substance | impurities  |
+-----------+-------------|------------------|-------------|
|    L01-10 | 1007.67     | 102.88           | 1.00100     |
|    L01-06 |  996.42     | 99.68            | 2.00087     |
|    G02-03 | 1111.95     | 125.04           | 3.00004     |
|    G03-06 |  989.01     | 119.00           | 4.00062     |
+-----------+-------------+-------------+-------------+-----
```
* A inicialização da classe pode ser feita a partir da lista de listas do Python (ou nada) e armazenada na instância
variável chamada `data` conforme exemplo abaixo:
```
>>> my_drug_data = [
...                 ['L01-10', 1007.67, 102.88, 1.00100],
...                 ['L01-06', 996.42, 99.68, 2.00087],
...                 ['G02-03', 1111.95, 125.04, 3.00100],
...                 ['G03-06', 989.01, 119.00, 4.00004]
... ]
>>> my_analyzer = DrugAnalyzer(my_drug_data)
>>> my_analyzer.data
[['L01-10', 1007.67, 102.88, 1.001], ['L01-06', 996.42, 99.68, 2.00087], ['G02-03', 1111.95, 125.04, 3.001], ['G03-06', 989.01, 119.0, 4.00004]]
>>> DrugAnalyzer().data
[]
``` 
* A classe também deve ter a opção de adicionar listas únicas ao objeto. Adicionando uma lista ao objeto `DrugAnalyzer`
deve retornar uma nova instância deste objeto com um elemento adicional. Adicionando tipo impróprio ou uma lista com
length deve gerar um `ValueError`. Um exemplo de uma saída de adição correta e errada é mostrado abaixo:
```
>>> my_new_analyzer = my_analyzer + ['G03-01', 789.01, 129.00, 0.00008]
>>> my_new_analyzer.data
[['L01-10', 1007.67, 102.88, 1.001], ['L01-06', 996.42, 99.68, 2.00087], ['G02-03', 1111.95, 125.04, 3.001], ['G03-06', 989.01, 119.0, 4.00004], ['G03-01', 789.01, 129.0, 8e-05]]
>>> my_new_analyzer = my_analyzer + ['G03-01', 129.00, 0.00008]
Traceback (the most recent call is displayed as the last one):
  File "<stdin>", line 1, in <module>
ValueError: Improper length of the added list.
``` 

### Part 2
Implemente o método `verify_series` dentro da classe `app.drug_analyzer.DrugAnalyzer`.

O objetivo deste método é receber uma lista de parâmetros e usá-los para verificar se as pílulas descritas dentro da instância variável `data` corresponde aos critérios fornecidos. Deve retornar um valor `Boolean` como resultado.

A função seria chamada da seguinte forma:
```
verify_series(series_id = 'L01', act_subst_wgt = 100, act_subst_rate = 0,05, allowed_imp = 0,001)
```
Where:
 * o `series_id` é uma string de 3 caracteres que está presente no início de cada `pill_id`, antes do sinal `-`, por exemplo, `L01` é o `series_id` em `pill_id = L01-12`.

 * o `act_subst_wgt` é o peso esperado (_mg_) do conteúdo da substância ativa na série fornecida em um comprimido.

 * o `act_subst_rate` é a taxa permitida de diferença entre o peso da substância ativa e o esperado (`act_subst_wgt`). 
    Por exemplo, para `100 mg`, os valores aceitos seriam entre `95` e `105`.

 * o `allowed_imp` é a taxa permitida de substâncias impuras no `pill_weight`. Por exemplo, para `1000 mg` pill_weight
    e taxa de `0,001`, a quantidade permitida de impurezas é de `1 mg`.

A função deve tomar todos os comprimidos que fazem parte do `L01` série, some seus pesos e calcule se o
quantidade de `active_substance`, assim como `impurities`, corresponder às taxas indicadas. 

Deve retornar `True` se ambas as condições forem atendidas 
e `False` se alguma delas não for atendida.



O `False` resultado deve significar que todos os parâmetros passados ​​são adequados, mas o `active_substance` quantidade ou o `impurities` quantia é impróprio.
No caso de um`series_id` que não está presente no `data` ou no caso de qualquer parâmetro impróprio, a função deve lançar um `ValueError`.

Example:
```
>>> my_drug_data = [
...                 ['L01-10', 1000.02, 102.88, 1.00100],
...                 ['L01-06', 999.90, 96.00, 2.00087],
...                 ['G02-03', 1000, 96.50, 3.00100],
...                 ['G03-06', 989.01, 119.00, 4.00004]
... ]
>>> my_analyzer = DrugAnalyzer(my_drug_data)
>>> my_analyzer.verify_series(series_id = 'L01', act_subst_wgt = 100, act_subst_rate = 0.05, allowed_imp = 0.001)
False
>>> // O peso total de active_substances seria 198,88, que está dentro da taxa de 0.05 for 200 mg (2 * act_subst_wgt).
>>> // No entanto, a soma de impurezas seria 3,00187, que é mais do que 0.001*1999.92 (allowed_imp_rate * (1000.02 + 999.90).
>>> my_analyzer.verify_series(series_id = 'L01', act_subst_wgt = 100, act_subst_rate = 0.05, allowed_imp = 0.01)
True
>>> my_analyzer.verify_series(series_id = 'B03', act_subst_wgt = 100, act_subst_rate = 0.05, allowed_imp = 0.001)
Traceback (the most recent call is displayed as the last one):
  File "<stdin>", line 1, in <module>
ValueError: B03 series is not present within the dataset.
```
```
Para executar os testes de unidade, use:
python setup.py pytest
```
