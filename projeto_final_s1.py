# =====================================================
# PROJETO FINAL - SEMESTRE 1
# Análise Exploratória da Base HR
# Aluno: Stefano Laurito
# =====================================================

import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# =====================================================
# ETAPA 1 - IMPORTAÇÃO DOS ARQUIVOS CSV
# =====================================================

pasta_projeto = Path(__file__).parent

caminho_query1 = pasta_projeto / "consultas" / "query1.csv"
caminho_query2 = pasta_projeto / "consultas" / "query2.csv"

df_salarios = pd.read_csv(caminho_query1)
df_regioes = pd.read_csv(caminho_query2)

# =====================================================
# ETAPA 2 - VISUALIZAÇÃO INICIAL DOS DADOS
# =====================================================

print("=" * 60)
print("QUERY 1 - SALÁRIOS POR DEPARTAMENTO E CARGO")
print("=" * 60)
print(df_salarios.head())

print()

print("=" * 60)
print("QUERY 2 - FUNCIONÁRIOS POR REGIÃO")
print("=" * 60)
print(df_regioes.head())

# =====================================================
# ETAPA 3 - INFORMAÇÕES GERAIS
# =====================================================

print("\nINFORMAÇÕES DA QUERY 1")
df_salarios.info()

print("\nINFORMAÇÕES DA QUERY 2")
df_regioes.info()

# =====================================================
# ETAPA 4 - VERIFICAÇÃO DE VALORES NULOS
# =====================================================

print("\n" + "=" * 60)
print("VALORES NULOS - QUERY 1")
print("=" * 60)

print(df_salarios.isnull().sum())

print("\n" + "=" * 60)
print("VALORES NULOS - QUERY 2")
print("=" * 60)

print(df_regioes.isnull().sum())

print("\nANÁLISE DOS VALORES NULOS")

if df_salarios.isnull().sum().sum() == 0:
    print("A Query 1 não apresentou valores nulos.")
else:
    print("A Query 1 possui valores nulos que precisam de tratamento.")

if df_regioes["STATE_PROVINCE"].isnull().sum() == 1:
    print("A Query 2 apresentou apenas um valor nulo na coluna STATE_PROVINCE.")
    print("Como representa apenas um registro e não interfere nas análises salariais e geográficas, o dado será mantido.")

# =====================================================
# ETAPA 5 - VERIFICAÇÃO DE DUPLICATAS
# =====================================================

print("\n" + "=" * 60)
print("REGISTROS DUPLICADOS")
print("=" * 60)

duplicados_q1 = df_salarios.duplicated().sum()
duplicados_q2 = df_regioes.duplicated().sum()

print(f"Duplicados na Query 1: {duplicados_q1}")
print(f"Duplicados na Query 2: {duplicados_q2}")

# =====================================================
# ETAPA 6 - ESTATÍSTICAS DESCRITIVAS DOS SALÁRIOS
# =====================================================

print("\n" + "=" * 60)
print("ESTATÍSTICAS DESCRITIVAS DOS SALÁRIOS")
print("=" * 60)

media = df_salarios["SALARY"].mean()
mediana = df_salarios["SALARY"].median()
desvio = df_salarios["SALARY"].std()
moda = df_salarios["SALARY"].mode()[0]
maior = df_salarios["SALARY"].max()
menor = df_salarios["SALARY"].min()
quantidade = df_salarios["SALARY"].count()

print(f"Média salarial: {media:.2f}")
print(f"Mediana salarial: {mediana:.2f}")
print(f"Desvio padrão: {desvio:.2f}")
print(f"Moda: {moda}")
print(f"Maior salário: {maior}")
print(f"Menor salário: {menor}")
print(f"Quantidade de funcionários: {quantidade}")

# =====================================================
# ETAPA 7 - AGRUPAMENTOS
# =====================================================

print("\n" + "=" * 60)
print("SALÁRIO MÉDIO POR DEPARTAMENTO")
print("=" * 60)

salario_departamento = (
    df_salarios
    .groupby("DEPARTMENT_NAME")["SALARY"]
    .mean()
    .sort_values(ascending=False)
)

print(salario_departamento)

print("\n" + "=" * 60)
print("SALÁRIO MÉDIO POR CARGO")
print("=" * 60)

salario_cargo = (
    df_salarios
    .groupby("JOB_TITLE")["SALARY"]
    .mean()
    .sort_values(ascending=False)
)

print(salario_cargo)

print("\n" + "=" * 60)
print("QUANTIDADE DE FUNCIONÁRIOS POR REGIÃO")
print("=" * 60)

funcionarios_regiao = (
    df_regioes
    .groupby("REGION_NAME")["EMPLOYEE_ID"]
    .count()
    .sort_values(ascending=False)
)

print(funcionarios_regiao)

print("\n" + "=" * 60)
print("QUANTIDADE DE FUNCIONÁRIOS POR PAÍS")
print("=" * 60)

funcionarios_pais = (
    df_regioes
    .groupby("COUNTRY_NAME")["EMPLOYEE_ID"]
    .count()
    .sort_values(ascending=False)
)

print(funcionarios_pais)

print("\n" + "=" * 60)
print("QUANTIDADE DE FUNCIONÁRIOS POR DEPARTAMENTO")
print("=" * 60)

funcionarios_departamento = (
    df_salarios
    .groupby("DEPARTMENT_NAME")["EMPLOYEE_ID"]
    .count()
    .sort_values(ascending=False)
)

print(funcionarios_departamento)

print("\n" + "=" * 60)
print("TOP 10 MAIORES SALÁRIOS")
print("=" * 60)

top_salarios = (
    df_salarios
    .sort_values(by="SALARY", ascending=False)
    .head(10)
)

print(top_salarios)

# =====================================================
# ETAPA 8 - GRÁFICOS
# =====================================================

# Gráfico 1 - Salário médio por departamento

plt.figure(figsize=(10,6))

salario_departamento.plot(kind="barh")

for i, v in enumerate(salario_departamento):
    plt.text(v + 100, i, f"{v:.0f}", va="center")

plt.title("Salário Médio por Departamento")
plt.ylabel("Departamento")
plt.xlabel("Salário Médio")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("graficos/salario_medio_departamento.png")

plt.show()



# Gráfico 2 - Quantidade de Funcionários por Departamento

plt.figure(figsize=(10,6))

funcionarios_departamento.plot(kind="barh", color="orange")

for i, v in enumerate(funcionarios_departamento):
    plt.text(v + 0.5, i, str(v), va="center")

plt.title("Quantidade de Funcionários por Departamento")
plt.ylabel("Departamento")
plt.xlabel("Quantidade")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("graficos/funcionarios_departamento.png")

plt.show()



# Gráfico 3 - Funcionários por Região

plt.figure(figsize=(6,5))

funcionarios_regiao.plot(kind="bar", color="green")

for i, v in enumerate(funcionarios_regiao):
    plt.text(i, v + 1, str(v), ha="center")

plt.title("Funcionários por Região")
plt.xlabel("Região")
plt.ylabel("Quantidade")

plt.tight_layout()

plt.savefig("graficos/funcionarios_regiao.png")

plt.show()


# Gráfico 4 - Histrograma da Distribuição dos Salários

plt.figure(figsize=(10,6))

plt.hist(
    df_salarios["SALARY"],
    bins=10,
    edgecolor="black"
)

plt.title("Distribuição dos Salários")
plt.xlabel("Salário")
plt.ylabel("Quantidade de Funcionários")

plt.tight_layout()

plt.savefig("graficos/histograma_salarios.png")

plt.show()


# Gráfico 5 - Boxplot dos Salários

plt.figure(figsize=(8,6))

plt.boxplot(
    df_salarios["SALARY"],
    vert=True
)

plt.title("Boxplot dos Salários")
plt.ylabel("Salário")

plt.tight_layout()

plt.savefig("graficos/boxplot_salarios.png")

plt.show()

# =====================================================
# ETAPA 9 - CONCLUSÕES
# =====================================================

print("\n" + "=" * 60)
print("CONCLUSÕES DA ANÁLISE")
print("=" * 60)

print("- Foram analisados 106 funcionários da base HR.")
print(f"- O salário médio encontrado foi de R$ {media:.2f}.")
print(f"- O maior salário foi de R$ {maior} e o menor de R$ {menor}.")
print("- O departamento Executive apresentou a maior média salarial.")
print("- O departamento Shipping concentra a maior quantidade de funcionários.")
print("- A maior parte dos funcionários está localizada na região Americas.")
print("- Foi identificado apenas um valor nulo na coluna STATE_PROVINCE.")
print("- Não foram encontrados registros duplicados.")

print("\nProjeto finalizado com sucesso!")