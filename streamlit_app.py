import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ventas por Categoría", page_icon="📊")

st.title("📊 Dashboard simple de ventas por categoría")

# ---------------------------------------------------------
# Cargar CSV directamente desde GitHub (raw)
url = "https://raw.githubusercontent.com/wlegon-cloud/ventasessen/main/data/ventas_por_familia.csv"
df = pd.read_csv(url)

# ---------------------------------------------------------

# Convertir a formato largo (Año / Valor)
df_long = df.melt(id_vars=df.columns[0], var_name="Año", value_name="Valor")
df_long.rename(columns={df.columns[0]: "Categoria"}, inplace=True)

# Selector
categorias = df_long["Categoria"].unique()
cats_sel = st.multiselect("Seleccionar categorías:", categorias, default=categorias[:5])

# Filtrar
df_filtrado = df_long[df_long["Categoria"].isin(cats_sel)]

st.subheader("📈 Evolución por año")
st.line_chart(df_filtrado, x="Año", y="Valor", color="Categoria")

st.subheader("📋 Tabla filtrada")
st.dataframe(df_filtrado)
