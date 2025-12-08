import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ventas por Familia", page_icon="📊")
st.title("📊 Dashboard: Ventas por Familia")

url = "https://raw.githubusercontent.com/wlegon-cloud/ventasessen/main/data/ventas_por_familia.csv"
df = pd.read_csv(url)

# Supongo que la primera columna es la categoría/familia
df_long = df.melt(id_vars=df.columns[0], var_name="Año", value_name="Valor")
df_long.rename(columns={df.columns[0]: "Categoria"}, inplace=True)

categorias = df_long["Categoria"].unique()
cats_sel = st.multiselect("Seleccionar categorías:", categorias, default=list(categorias)[:5])

df_filtrado = df_long[df_long["Categoria"].isin(cats_sel)]

st.subheader("📈 Evolución por año")
st.line_chart(df_filtrado, x="Año", y="Valor", color="Categoria")

st.subheader("📋 Datos filtrados")
st.dataframe(df_filtrado)
