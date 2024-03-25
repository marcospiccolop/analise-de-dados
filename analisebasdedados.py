import pandas as pd

tabela = pd.read_csv("cancelamentos.csv")
tabela = tabela.drop(columns="CustomerID")
print(tabela)
# Obtendo informações da tabela
print(tabela.info())

# Escluindo valores vazios da tabela dropna
tabela = tabela.dropna()
print(tabela.info())

# Contar, analisar os valores de uma coluna !!
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True))

#formatando o valor da poprcentagem

tabela = tabela [tabela["duracao_contrato"]!="Monthly"]
tabela = tabela [tabela["ligacoes_callcenter"]<=4]
tabela = tabela [tabela["dias_atraso"]<=20]

print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

#analisar as causas dos cancelamentos - CRIANDO GRÁFICOS

#import plotly.express as px

#DOIS PASSOS... CRIAR O GRAFICO DEPOIS EXIBIR
#for coluna in tabela.columns:
  #  grafico = px.histogram(tabela, x=coluna, color="cancelou")
 #   grafico.show()

