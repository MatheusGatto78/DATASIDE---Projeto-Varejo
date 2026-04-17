import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

try:
    df = pd.read_csv('Retail_Transactions_Dataset.csv')
except FileNotFoundError:
    print("Erro: O arquivo 'Retail_Transactions_Dataset.csv' não foi encontrado. Certifique-se de que o arquivo está no diretório correto.")
except Exception as e:
    print(f"Ocorreu um erro ao carregar o dataset: {e}")

if 'df' not in locals():
    sys.exit(1)

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

# # Qual o método escolhido para as compras mais caras?
# # Agrupar por método de pagamento e somar o Total_Cost para cada um
# compras_mais_caras_por_metodo = df.groupby('Payment_Method')['Total_Cost'].sum().sort_values(ascending=False)
# print("\nMétodo de pagamento para compras mais caras (somatório de Total_Cost):")
# print(compras_mais_caras_por_metodo)
# # Visualização
# plt.figure(figsize=(10, 6))
# sns.barplot(
#     x=compras_mais_caras_por_metodo.index,
#     y=compras_mais_caras_por_metodo.values,
#     hue=compras_mais_caras_por_metodo.index,
#     palette='plasma',
#     legend=False,
# )
# plt.title('Método de Pagamento por Valor Total de Vendas')
# plt.xlabel('Método de Pagamento')
# plt.ylabel('Valor Total de Vendas (R$)')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # Qual a quantidade de vendas por hora?
# if 'Date' in df.columns:
#     try:
#         df['Date'] = pd.to_datetime(df['Date'])
#         df['Hour'] = df['Date'].dt.hour
#         print("Coluna 'Hour' criada a partir da coluna 'Date'.")
#
#         vendas_por_hora = df.groupby('Hour')['Total_Items'].sum()
#         print("\nQuantidade de vendas por hora:")
#         print(vendas_por_hora)
#
#         # Visualização
#         plt.figure(figsize=(12, 7))
#         sns.lineplot(x=vendas_por_hora.index, y=vendas_por_hora.values, marker='o')
#         plt.title('Quantidade de Vendas por Hora do Dia')
#         plt.xlabel('Hora do Dia')
#         plt.ylabel('Quantidade de Itens Vendidos')
#         plt.xticks(range(0, 24))
#         plt.tight_layout()
#         plt.show()
#     except Exception as e:
#         print(f"Erro ao processar a coluna 'Date' para análise por hora: {e}")
# else:
#     print("Coluna 'Date' não encontrada no dataset. Não foi possível realizar a análise de vendas por hora.")
#
# # Qual a quantidade de vendas por dia da semana?
# if 'Date' in df.columns:
#     # Converte a coluna Date para datetime e remove registros com data invalida.
#     df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
#     df_valid = df.dropna(subset=['Date']).copy()
#
#     dias_ordenados = [
#         'Segunda-feira',
#         'Terça-feira',
#         'Quarta-feira',
#         'Quinta-feira',
#         'Sexta-feira',
#         'Sábado',
#         'Domingo',
#     ]
#     mapa_dias = {
#         0: 'Segunda-feira',
#         1: 'Terça-feira',
#         2: 'Quarta-feira',
#         3: 'Quinta-feira',
#         4: 'Sexta-feira',
#         5: 'Sábado',
#         6: 'Domingo',
#     }
#
#     df_valid['DayOfWeek'] = df_valid['Date'].dt.dayofweek.map(mapa_dias)
#     df_valid['DayOfWeek'] = pd.Categorical(df_valid['DayOfWeek'], categories=dias_ordenados, ordered=True)
#
#     vendas_por_dia_semana = df_valid.groupby('DayOfWeek')['Total_Items'].sum().reindex(dias_ordenados, fill_value=0)
#     print("\nQuantidade de vendas por dia da semana:")
#     print(vendas_por_dia_semana)
#
#     # Visualização
#     plt.figure(figsize=(12, 7))
#     sns.barplot(
#         x=vendas_por_dia_semana.index,
#         y=vendas_por_dia_semana.values,
#         hue=vendas_por_dia_semana.index,
#         palette='coolwarm',
#         legend=False,
#     )
#     plt.title('Quantidade de Vendas por Dia da Semana')
#     plt.xlabel('Dia da Semana')
#     plt.ylabel('Quantidade de Itens Vendidos')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()
# else:
#     print("Não foi possível realizar a análise de vendas por dia da semana devido à falta da coluna 'Date'.")

# # O dia e hora com mais venda por cidade?
# if 'Date' in df.columns and 'City' in df.columns:
#     df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
#     df_valid = df.dropna(subset=['Date']).copy()
#
#     mapa_dias = {
#         0: 'Segunda-feira',
#         1: 'Terça-feira',
#         2: 'Quarta-feira',
#         3: 'Quinta-feira',
#         4: 'Sexta-feira',
#         5: 'Sábado',
#         6: 'Domingo',
#     }
#
#     df_valid['Hour'] = df_valid['Date'].dt.hour
#     df_valid['DayOfWeek'] = df_valid['Date'].dt.dayofweek.map(mapa_dias)
#
#     vendas_por_cidade_dia_hora = df_valid.groupby(['City', 'DayOfWeek', 'Hour'])['Total_Items'].sum().reset_index()
#
#     # Encontrar o dia e hora com mais vendas para cada cidade
#     idx = vendas_por_cidade_dia_hora.groupby('City')['Total_Items'].idxmax()
#     melhor_horario_por_cidade = vendas_por_cidade_dia_hora.loc[idx]
#
#     print("\nDia e hora com mais vendas por cidade:")
#     print(melhor_horario_por_cidade)
#
#     # Visualização (exemplo para as top N cidades)
#     top_n_cidades = melhor_horario_por_cidade.nlargest(5, 'Total_Items')  # Top 5 cidades com mais vendas
#     plt.figure(figsize=(14, 8))
#     sns.barplot(x='City', y='Total_Items', hue='DayOfWeek', data=top_n_cidades, palette='tab10')
#     plt.title('Dia e Hora de Pico de Vendas por Cidade (Top 5 Cidades)')
#     plt.xlabel('Cidade')
#     plt.ylabel('Quantidade de Itens Vendidos')
#     plt.xticks(rotation=45)
#     plt.legend(title='Dia da Semana', bbox_to_anchor=(1.05, 1), loc='upper left')
#     plt.tight_layout()
#     plt.show()
# else:
#     print("Não foi possível realizar a análise de vendas por cidade, dia e hora devido à falta das colunas 'Date' ou 'City'.")

# Setor escolhido para todas as proximas analises.
store_type_escolhido = 'Warehouse Club'
df_setor = df[
    df['Store_Type'].fillna('').str.strip().str.casefold()
    == store_type_escolhido.casefold()
].copy()

if df_setor.empty:
    print(f"Nenhum registro encontrado para o setor: {store_type_escolhido}")
    sys.exit(1)

print(f"Setor escolhido: {store_type_escolhido}")
print(f"Total de transacoes no setor: {len(df_setor)}")

# Na coluna Product temos mais de um item por transacao; separar e agrupar por item.
# Objetivo: descobrir qual item do setor escolhido apareceu com maior frequencia.
if 'Product' in df_setor.columns:
    itens_por_transacao = (
        df_setor['Product']
        .fillna('')
        .astype(str)
        .str.split(r'\s*[;,|]\s*', regex=True)
    )

    itens_explodidos = (
        itens_por_transacao
        .explode()
        .astype(str)
        .str.strip()
        .str.strip("[]'\"")
        .str.strip()
    )
    itens_explodidos = itens_explodidos[itens_explodidos != '']

    frequencia_itens = itens_explodidos.value_counts()

    if not frequencia_itens.empty:
        item_mais_vendido = frequencia_itens.index[0]
        frequencia_item_mais_vendido = int(frequencia_itens.iloc[0])

        print("\nFrequencia de itens no setor (top 10):")
        print(frequencia_itens.head(10))
        print(
            f"\nItem que mais vendeu no setor {store_type_escolhido}: "
            f"{item_mais_vendido} ({frequencia_item_mais_vendido} ocorrencias)"
        )
    else:
        print("\nNao foi possivel calcular a frequencia de itens: coluna Product sem valores validos.")
else:
    print("\nColuna 'Product' nao encontrada no recorte do setor.")

# Qual item no setor vendeu menos (apareceu com menos frequencia)?
if 'frequencia_itens' in locals() and not frequencia_itens.empty:
    menor_frequencia = int(frequencia_itens.min())
    itens_menos_vendidos = frequencia_itens[frequencia_itens == menor_frequencia].sort_index()

    print("\nItem(ns) que vendeu(ram) menos no setor:")
    print(itens_menos_vendidos)
else:
    print("\nNao foi possivel identificar o item menos vendido no setor.")

# Qual item cada perfil de cliente compra mais?
if (
    'itens_explodidos' in locals()
    and not itens_explodidos.empty
    and 'Customer_Category' in df_setor.columns
):
    itens_por_perfil = pd.DataFrame(
        {
            'Customer_Category': df_setor.loc[itens_explodidos.index, 'Customer_Category'].astype(str),
            'Item': itens_explodidos.values,
        }
    )

    itens_por_perfil['Customer_Category'] = itens_por_perfil['Customer_Category'].str.strip()
    itens_por_perfil['Item'] = itens_por_perfil['Item'].astype(str).str.strip()
    itens_por_perfil = itens_por_perfil[
        (itens_por_perfil['Customer_Category'] != '')
        & (itens_por_perfil['Item'] != '')
    ]

    contagem_perfil_item = (
        itens_por_perfil
        .groupby(['Customer_Category', 'Item'])
        .size()
        .reset_index(name='Frequencia')
    )

    idx_top_item_perfil = contagem_perfil_item.groupby('Customer_Category')['Frequencia'].idxmax()
    item_mais_comprado_por_perfil = (
        contagem_perfil_item.loc[idx_top_item_perfil]
        .sort_values('Customer_Category')
        .reset_index(drop=True)
    )

    print("\nItem que cada perfil de cliente compra mais:")
    print(item_mais_comprado_por_perfil)
else: 
    print("\nNao foi possivel calcular o item mais comprado por perfil de cliente.")