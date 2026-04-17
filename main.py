import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

try:
    df = pd.read_csv('Retail_Transactions_Dataset.csv')
    print("Dataset carregado com sucesso!")
    print("\nPrimeiras 5 linhas do dataset:")
    print(df.head())
    print("\nInformações gerais do dataset:")
    df.info()
    print("\nEstatísticas descritivas do dataset:")
    print(df.describe())
except FileNotFoundError:
    print("Erro: O arquivo 'Retail_Transactions_Dataset.csv' não foi encontrado. Certifique-se de que o arquivo está no diretório correto.")
except Exception as e:
    print(f"Ocorreu um erro ao carregar o dataset: {e}")

print("\nValores ausentes por coluna:")
print(df.isnull().sum())

print("\nTipos de dados por coluna:")
print(df.dtypes)

print(f"\nNúmero de linhas duplicadas antes da remoção: {df.duplicated().sum()}")
df.drop_duplicates(inplace=True)
print(f"Número de linhas após remoção de duplicatas: {len(df)}")