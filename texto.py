def nao_primo():
  lista = [7, 11, 13, 17, 19, 23, 29, 31]
  segunda_lista = []

  for item in lista:
    for outro_item in lista:
      produto = item * outro_item
      modulo = produto % 30
      if(modulo == 1):
        modulo = 30 + modulo
      divisao = produto // 30
      tupla = (item, outro_item, produto, divisao, modulo)
      segunda_lista.append(tupla)
  return segunda_lista

a = nao_primo()

import pandas as pd

pd.set_option('display.max_rows', None)

df = pd.DataFrame(a)
display(df.rename(columns={0: 'Primeiro Valor',1: 'Segundo Valor',2: 'Produto',
                          3: 'Parte Inteira da Divisao', 4: 'Resto da Divisao'}))
