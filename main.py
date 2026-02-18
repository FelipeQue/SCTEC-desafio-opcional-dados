# Importação das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregamento dos dados
df = pd.read_csv('titanic_dataset.csv')

# Reconhecimento dos dados
#print(df.info())
#print(df.describe())

# Limpeza dos dados: verificação de linhas duplicadas
duplicate_rows = df[df.duplicated()]
print(f"Número de linhas duplicadas: {len(duplicate_rows)}")

if len(duplicate_rows) > 0:
    print(f'Número de linhas antes da limpeza: {len(df)}')
    df.drop_duplicates(keep='last',inplace=True).reset_index(drop=True)
    print(f'Número de linhas após a limpeza: {len(df)}')
else:
    print("Não há linhas duplicadas para remover.")

# Limpeza dos dados: verificação de valores nulos
print("Número de valores nulos por coluna:")
print(df.isnull().sum())


# Taxa de sobrevivência geral
print(f"Total de sobreviventes: {df['Survived'].sum()}")
print(f"Total de não sobreviventes: {len(df) - df['Survived'].sum()}")

survival_rate = df['Survived'].mean() * 100
print(f"Taxa de sobrevivência geral: {survival_rate:.2f}%")

# Análise de sexo e sobrevivência

print(f"Total de homens: {len(df[df['Sex'] == 'male'])}")
male_percentage = (df["Sex"] == "male").mean() * 100
print(f"Porcentagem de homens: {male_percentage:.2f}%")
print(f"Total de mulheres: {len(df[df['Sex'] == 'female'])}")
female_percentage = (df["Sex"] == "female").mean() * 100
print(f"Porcentagem de mulheres: {female_percentage:.2f}%")

print(f"Total de homens sobreviventes: {len(df[(df['Sex'] == 'male') & (df['Survived'] == 1)])}")
male_survivors_percentage = (df[(df['Sex'] == 'male') & (df['Survived'] == 1)]).shape[0] / len(df[df['Sex'] == 'male']) * 100
print(f"Porcentagem de homens sobreviventes: {male_survivors_percentage:.2f}%")
print(f"Total de mulheres sobreviventes: {len(df[(df['Sex'] == 'female') & (df['Survived'] == 1)])}")
female_survivors_percentage = (df[(df['Sex'] == 'female') & (df['Survived'] == 1)]).shape[0] / len(df[df['Sex'] == 'female']) * 100
print(f"Porcentagem de mulheres sobreviventes: {female_survivors_percentage:.2f}%")

# Gráficos de pizza: proporção de homens e mulheres
order = ['male', 'female']
sex_counts = df['Sex'].value_counts().reindex(order)
colors = ['#00F5D4', '#A44CD3']
custom_labels = ['Homens', 'Mulheres']
plt.figure(figsize=(8, 6))
plt.pie(sex_counts, labels=custom_labels, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Proporção de Homens e Mulheres')
plt.show()

survived_sex_counts = df[df['Survived'] == 1]['Sex'].value_counts().reindex(order)
plt.pie(survived_sex_counts, labels=custom_labels, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Proporção de Homens e Mulheres Sobreviventes')
plt.show()


