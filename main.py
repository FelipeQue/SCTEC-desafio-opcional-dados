# Importação das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregamento dos dados
df = pd.read_csv('titanic_dataset.csv')

# Reconhecimento dos dados
print(df.info())
print(df.describe())

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
total_male = (df["Sex"] == "male").sum()
total_female = (df["Sex"] == "female").sum()

male_percentage = (df["Sex"] == "male").mean() * 100
female_percentage = (df["Sex"] == "female").mean() * 100

male_survivors = ((df["Sex"] == "male") & (df["Survived"] == 1)).sum()
female_survivors = ((df["Sex"] == "female") & (df["Survived"] == 1)).sum()

male_survivors_percentage = ((df["Sex"] == "male") & (df["Survived"] == 1)).mean() / (df["Sex"] == "male").mean() * 100
female_survivors_percentage = ((df["Sex"] == "female") & (df["Survived"] == 1)).mean() / (df["Sex"] == "female").mean() * 100

print(f"Total de homens: {total_male}")
print(f"Porcentagem de homens: {male_percentage:.2f}%")
print(f"Total de mulheres: {total_female}")
print(f"Porcentagem de mulheres: {female_percentage:.2f}%")

print(f"Total de homens sobreviventes: {male_survivors}")
print(f"Porcentagem de homens sobreviventes: {male_survivors_percentage:.2f}%")
print(f"Total de mulheres sobreviventes: {female_survivors}")
print(f"Porcentagem de mulheres sobreviventes: {female_survivors_percentage:.2f}%")

# Gráficos de pizza: proporção de homens e mulheres entre pessoas passageiras e entre sobreviventes
order = ['male', 'female']
sex_counts = df['Sex'].value_counts().reindex(order)
colors = ['#00F5D4', '#A44CD3']
custom_labels = ['Homens', 'Mulheres']
plt.figure(figsize=(8, 6))
plt.pie(sex_counts, labels=custom_labels, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Proporção de homens e mulheres no navio')
plt.show()

survived_sex_counts = df[df['Survived'] == 1]['Sex'].value_counts().reindex(order)
plt.pie(survived_sex_counts, labels=custom_labels, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Proporção de homens e mulheres sobreviventes')
plt.show()


# Correlação entre classe no navio e tarifa
class_fare_analysis = df.groupby('Pclass')['Fare'].agg(['mean', 'median', 'min', 'max', 'count'])
print("Análise da tarifa por classe no navio:")
print(class_fare_analysis)

class_fare_corr = df[['Pclass','Fare']].corr(method='pearson')
print("Correlação pelo método Pearson entre classe no navio e tarifa:", class_fare_corr)


# Gráfico de violino para visualizar a distribuição das tarifas por classe no navio
social_class_grouped = df.groupby('Pclass')['Fare']
social_class_data = [social_class_grouped.get_group(pclass).values for pclass in sorted(social_class_grouped.groups.keys())]
plt.figure(figsize=(8, 6))
plt.title('Relação entre Classe no Navio e Tarifa')
plt.xlabel('Classe no Navio')
plt.ylabel('Tarifa')
plt.violinplot(social_class_data, positions=[1, 2, 3])
plt.xticks([1, 2, 3])
plt.grid()
plt.show()


# Análise de classe social e sobrevivência
class_survival_rate = df.groupby('Pclass')['Survived'].mean() * 100
print("Taxa de sobrevivência por classe:")
print(class_survival_rate)

# Gráfico de barras da taxa de sobrevivência por classe
colors = ['#FFD700', '#A9A9A9', '#2F4F4F']  # Ouro (rico), Cinza (médio), Cinza escuro (pobre)
sns.barplot(x=class_survival_rate.index, y=class_survival_rate.values, hue=class_survival_rate.index, palette=colors, legend=False)
plt.title("Taxa de sobrevivência por classe social")
plt.xlabel("Classe no Navio")
plt.ylabel("Taxa de sobrevivência (%)")
plt.xticks([0, 1, 2], ['1ª Classe', '2ª Classe', '3ª Classe'])
plt.show()

class_survival_corr = df[['Pclass','Survived']].corr(method='spearman')
print("Correlação pelo método Spearman entre classe no navio e sobrevivência:", class_survival_corr)
