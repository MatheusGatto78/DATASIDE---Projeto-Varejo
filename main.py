import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

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

# Modelo de Machine Learning - combinacao de itens (Primeira Entrega)
# Tecnica escolhida: Algoritmo Apriori + regras de associacao.
try:
    from ast import literal_eval
    from mlxtend.frequent_patterns import apriori, association_rules

    if 'Transaction_ID' in df_setor.columns and 'Product' in df_setor.columns:
        def extrair_itens_produto(valor):
            if pd.isna(valor):
                return []

            texto = str(valor).strip()
            if not texto:
                return []

            # O dataset costuma vir como lista serializada em texto, ex: "['Milk', 'Bread']".
            if texto.startswith('[') and texto.endswith(']'):
                try:
                    lista = literal_eval(texto)
                    if isinstance(lista, list):
                        itens = [str(i).strip().strip("'\"") for i in lista if str(i).strip()]
                        return [i for i in itens if i]
                except (ValueError, SyntaxError):
                    pass

            itens = [p.strip().strip("'\"") for p in texto.split(',') if p.strip()]
            return [i for i in itens if i]

        transacoes = df_setor[['Transaction_ID', 'Product']].copy()
        transacoes['Itens'] = transacoes['Product'].apply(extrair_itens_produto)
        transacoes = transacoes[transacoes['Itens'].map(len) > 0]

        if transacoes.empty:
            print("\n[Apriori] Nao ha transacoes com itens validos para montar recomendacoes.")
        else:
            basket = (
                transacoes
                .explode('Itens')
                .assign(valor=1)
                .pivot_table(
                    index='Transaction_ID',
                    columns='Itens',
                    values='valor',
                    aggfunc='max',
                    fill_value=0,
                )
                .astype(bool)
            )

            itemsets_frequentes = apriori(basket, min_support=0.002, use_colnames=True)
            regras = association_rules(itemsets_frequentes, metric='confidence', min_threshold=0.05)

            if regras.empty:
                print("\n[Apriori] Nenhuma regra relevante encontrada com os parametros atuais.")
            else:
                regras = regras.sort_values(['lift', 'confidence', 'support'], ascending=False)

                regras_exibicao = regras.copy()
                regras_exibicao['antecedents'] = regras_exibicao['antecedents'].apply(
                    lambda x: ', '.join(sorted(list(x)))
                )
                regras_exibicao['consequents'] = regras_exibicao['consequents'].apply(
                    lambda x: ', '.join(sorted(list(x)))
                )

                colunas_saida = ['antecedents', 'consequents', 'support', 'confidence', 'lift']
                top10_regras = regras_exibicao[colunas_saida].head(10).copy()

                print("\n[Apriori] Top 10 regras de recomendacao para o setor Warehouse Club:")
                print(top10_regras.to_string(index=False))

                # Metricas para avaliacao do modelo.
                total_transacoes = basket.shape[0]
                total_itens_unicos = basket.shape[1]
                total_itemsets = len(itemsets_frequentes)
                total_regras = len(regras)
                lift_medio = regras['lift'].mean()
                confianca_media = regras['confidence'].mean()
                suporte_medio = regras['support'].mean()
                regras_com_lift_maior_1 = (regras['lift'] > 1).mean() * 100

                itens_recomendacao = set().union(*regras['antecedents']).union(*regras['consequents'])
                cobertura_itens = (len(itens_recomendacao) / total_itens_unicos) * 100 if total_itens_unicos else 0

                print("\n[Apriori] Justificativa da tecnica escolhida:")
                print(
                    "Apriori foi escolhido por ser um metodo classico, interpretavel e adequado "
                    "para recomendacao baseada em cestas de compra, permitindo identificar "
                    "itens frequentemente comprados juntos e transformar isso em regras acionaveis."
                )

                print("\n[Apriori] Metricas de avaliacao do modelo:")
                print(f"- Total de transacoes analisadas: {total_transacoes}")
                print(f"- Total de itens unicos: {total_itens_unicos}")
                print(f"- Itemsets frequentes encontrados: {total_itemsets}")
                print(f"- Regras de associacao geradas: {total_regras}")
                print(f"- Suporte medio das regras: {suporte_medio:.4f}")
                print(f"- Confianca media das regras: {confianca_media:.4f}")
                print(f"- Lift medio das regras: {lift_medio:.4f}")
                print(f"- Percentual de regras com lift > 1: {regras_com_lift_maior_1:.2f}%")
                print(f"- Cobertura de itens nas regras: {cobertura_itens:.2f}%")

                # Elementos visuais (graficos) para analise: salvos em arquivo.
                saida_dir = 'apriori_outputs'
                os.makedirs(saida_dir, exist_ok=True)

                # Tabela visual com Top 10 regras de associacao.
                tabela_visual = top10_regras.copy()
                tabela_visual['support'] = tabela_visual['support'].map(lambda x: f"{x:.4f}")
                tabela_visual['confidence'] = tabela_visual['confidence'].map(lambda x: f"{x:.4f}")
                tabela_visual['lift'] = tabela_visual['lift'].map(lambda x: f"{x:.4f}")

                fig, ax = plt.subplots(figsize=(14, 5.8))
                ax.axis('off')
                tabela = ax.table(
                    cellText=tabela_visual.values,
                    colLabels=['Antecedente', 'Consequente', 'Support', 'Confidence', 'Lift'],
                    loc='center',
                    cellLoc='center',
                )
                tabela.auto_set_font_size(False)
                tabela.set_fontsize(9)
                tabela.scale(1, 1.35)
                plt.title('Top 10 Regras de Associacao - Warehouse Club (Apriori)', pad=12)
                caminho_tabela = os.path.join(saida_dir, 'top10_regras_tabela.png')
                plt.savefig(caminho_tabela, dpi=150, bbox_inches='tight')
                plt.close()

                top_regras_grafico = regras_exibicao[colunas_saida].head(10).copy()
                top_regras_grafico['regra'] = (
                    top_regras_grafico['antecedents']
                    + ' -> '
                    + top_regras_grafico['consequents']
                )
                top_regras_grafico = top_regras_grafico.sort_values('lift', ascending=True)

                plt.figure(figsize=(12, 7))
                plt.barh(top_regras_grafico['regra'], top_regras_grafico['lift'], color='steelblue')
                plt.title('Top 10 Regras por Lift - Apriori (Warehouse Club)')
                plt.xlabel('Lift')
                plt.ylabel('Regra')
                plt.tight_layout()
                caminho_lift = os.path.join(saida_dir, 'top_regras_lift.png')
                plt.savefig(caminho_lift, dpi=150)
                plt.close()

                plt.figure(figsize=(10, 6))
                scatter = plt.scatter(
                    regras['support'],
                    regras['confidence'],
                    c=regras['lift'],
                    cmap='viridis',
                    alpha=0.7,
                )
                plt.colorbar(scatter, label='Lift')
                plt.title('Suporte vs Confianca das Regras (cor = Lift)')
                plt.xlabel('Support')
                plt.ylabel('Confidence')
                plt.tight_layout()
                caminho_scatter = os.path.join(saida_dir, 'suporte_confianca_lift.png')
                plt.savefig(caminho_scatter, dpi=150)
                plt.close()

                print("\n[Apriori] Graficos salvos:")
                print(f"- {caminho_tabela}")
                print(f"- {caminho_lift}")
                print(f"- {caminho_scatter}")
    else:
        print("\n[Apriori] Colunas necessarias nao encontradas: Transaction_ID e/ou Product.")
except ImportError:
    print("\n[Apriori] Biblioteca mlxtend nao instalada. Instale com: pip install mlxtend")
except Exception as e:
    print(f"\n[Apriori] Erro ao gerar recomendacoes: {e}")