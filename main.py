import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

try:
    df = pd.read_csv('Retail_Transactions_Dataset.csv')
except FileNotFoundError:
    print("Erro: O arquivo 'Retail_Transactions_Dataset.csv' não foi encontrado. Certifique-se de que o arquivo está no diretório correto.")
except Exception as e:
    print(f"Ocorreu um erro ao carregar o dataset: {e}")

# #  Qual o total de itens vendidos (somar a quantidade de todos os itens)?
# total_itens_vendidos = df['Total_Items'].sum()
# print(f"\nTotal de itens vendidos: {total_itens_vendidos}")

# # Qual o valor total de vendas?
# total_valor_vendas = df['Total_Cost'].sum()
# print(f"Total de valor de vendas: R$ {total_valor_vendas:.2f}")

# # Quantos itens cada Store_type vendeu e quantos % representa do total de itens vendidos?
# # Itens vendidos por Store_type
# total_itens_vendidos = df['Total_Items'].sum()
# itens_por_loja = df.groupby('Store_Type')['Total_Items'].sum().sort_values(ascending=False)
# print("\nItens vendidos por tipo de loja:")
# print(itens_por_loja)
# # Percentual de itens vendidos por Store_type
# percentual_itens_por_loja = (itens_por_loja / total_itens_vendidos) * 100
# print("\nPercentual de itens vendidos por tipo de loja:")
# print(percentual_itens_por_loja.apply(lambda x: f'{x:.2f}%'))
# # Visualização
# plt.figure(figsize=(12, 7))
# sns.barplot(x=itens_por_loja.index, y=itens_por_loja.values, hue=itens_por_loja.index, palette='viridis', legend=False)
# plt.title('Total de Itens Vendidos por Tipo de Loja')
# plt.xlabel('Tipo de Loja')
# plt.ylabel('Total de Itens Vendidos')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # Qual o total de custo por Store_type e qual o % do total de custos?
# total_custo_geral = df['Total_Cost'].sum()
# custo_por_loja = df.groupby('Store_Type')['Total_Cost'].sum().sort_values(ascending=False)
# print("\nTotal de custo por tipo de loja:")
# print(custo_por_loja)
# percentual_custo_por_loja = (custo_por_loja / total_custo_geral) * 100
# print("\nPercentual de custo por tipo de loja:")
# print(percentual_custo_por_loja.apply(lambda x: f'{x:.2f}%'))
# # Visualização
# plt.figure(figsize=(12, 7))
# sns.barplot(x=custo_por_loja.index, y=custo_por_loja.values, hue=custo_por_loja.index, palette='magma', legend=False)
# plt.title('Total de Custo por Tipo de Loja')
# plt.xlabel('Tipo de Loja')
# plt.ylabel('Total de Custo')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # Qual método de pagamento é mais usado e qual é menos usado?
# metodo_pagamento = df['Payment_Method'].value_counts()
# print("\nMétodos de pagamento mais e menos usados:")
# print(metodo_pagamento)
# # Visualização
# plt.figure(figsize=(10, 6))
# sns.barplot(x=metodo_pagamento.index, y=metodo_pagamento.values, palette='cividis')
# plt.title('Frequência dos Métodos de Pagamento')
# plt.xlabel('Método de Pagamento')
# plt.ylabel('Número de Transações')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# Qual o método escolhido para as compras mais caras?
# Agrupar por método de pagamento e somar o Total_Cost para cada um
compras_mais_caras_por_metodo = df.groupby('Payment_Method')['Total_Cost'].sum().sort_values(ascending=False)
print("\nMétodo de pagamento para compras mais caras (somatório de Total_Cost):")
print(compras_mais_caras_por_metodo)

# Visualização
plt.figure(figsize=(10, 6))
sns.barplot(
    x=compras_mais_caras_por_metodo.index,
    y=compras_mais_caras_por_metodo.values,
    hue=compras_mais_caras_por_metodo.index,
    palette='plasma',
    legend=False,
)
plt.title('Método de Pagamento por Valor Total de Vendas')
plt.xlabel('Método de Pagamento')
plt.ylabel('Valor Total de Vendas (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()