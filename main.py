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

# Qual o valor total de vendas?
total_valor_vendas = df['Total_Cost'].sum()
print(f"Total de valor de vendas: R$ {total_valor_vendas:.2f}")