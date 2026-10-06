import pandas as pd
import numpy as np

# Parte 1. Carga y exploracion inicial

df = pd.read_excel("movies.xlsx")

print("--- Dimensiones iniciales ---")
print(df.shape)

print("\n--- Primeras filas ---")
print(df.head())


# Parte 2. Estandarización de cadenas de texto

def extraer_director(texto):
    if pd.isna(texto) or 'Director:' not in str(texto):
        return np.nan
    director = str(texto).split('|')[0]
    return (director
            .replace('Director:', '')
            .replace('Directors:', '')
            .replace('\n', '')
            .replace('\r', '')
            .strip())

def extraer_reparto(texto):
    if pd.isna(texto):
        return np.nan
    if '|' in str(texto):
        parte = str(texto).split('|')[1]
    else:
        parte = str(texto)
    return (parte
            .replace('Stars:', '')
            .replace('\n', '')
            .replace('\r', '')
            .strip())

df['DIRECTOR'] = df['STARS'].apply(extraer_director)
df['REPARTO'] = df['STARS'].apply(extraer_reparto)


# EJERCICIO EVALUADO


# 3. Porcentaje de valores faltantes por columna
print("\n--- Pregunta 3: Valores faltantes ---")
porcentaje_faltantes = (df.isnull().sum() / len(df)) * 100
print(porcentaje_faltantes.sort_values(ascending=False))

# 4. Registros vacios en RunTime y estrategias
print("\n--- Pregunta 4: Análisis de RUNTIME ---")
# Corregido: La columna en tu Excel se llama RunTime, no RUNTIME
vacios_runtime = df['RunTime'].isnull().sum()
print(f"Cantidad de nulos en RunTime: {vacios_runtime}")
print(f"Media de RunTime: {df['RunTime'].mean():.2f}")
print(f"Mediana de RunTime: {df['RunTime'].median():.2f}")

# 5. Transformacion sin duplicados
print("\n--- Pregunta 5: Duplicados ---")
df_sin_duplicados = df.drop_duplicates()
print(f"Dimensiones originales: {df.shape}")
print(f"Dimensiones sin duplicados: {df_sin_duplicados.shape}")
duplicados = len(df) - len(df_sin_duplicados)
print(f"Cantidad de registros duplicados: {duplicados}")

# 6. Limpieza de YEAR
print("\n--- Pregunta 6: Limpieza de YEAR ---")
df['YEAR_CLEAN'] = df['YEAR'].astype(str).str.extract(r'([0-9]{4})')
print(df[['YEAR', 'YEAR_CLEAN']].dropna().head())

# 7. Registros con RATING = 0
print("\n--- Pregunta 7: RATING = 0.00 ---")
rating_cero = (df['RATING'] == 0.00).sum()
print(f"Registros con RATING 0.00: {rating_cero}")
df['RATING'] = df['RATING'].replace(0.00, np.nan)