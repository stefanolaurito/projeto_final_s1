# =====================================================
# PROJETO FINAL - SEMESTRE 1
# Análise Exploratória da Base HR
# Aluno: Stefano Laurito
# =====================================================

import pandas as pd
from pathlib import Path

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