import mysql.connector
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Conexión a MySQL
conn = mysql.connector.connect(
    host='bbp3sjiqssvggqn98zv7-mysql.services.clever-cloud.com',         
    database='bbp3sjiqssvggqn98zv7',
    user='uxua3zzo2tc0uvkj',     
    password='f8smPk0LobUDubjTdlYc'
    
)

# Cargar datos
query = "SELECT * FROM productos_papeleria"
df = pd.read_sql(query, conn)

st.set_page_config(page_title="Análisis Exploratorio", layout="wide")

st.title("📊 Análisis Exploratorio de Productos")

st.subheader("Primeros registros")
st.write(df.head())

st.subheader("Distribución de Precios")
fig, ax = plt.subplots()
sns.histplot(df['precio'], bins=20, kde=True, ax=ax)
st.pyplot(fig)

st.subheader("Gráfico de caja por categoría")
if 'categoria' in df.columns:
    fig2, ax2 = plt.subplots()
    sns.boxplot(data=df, x='categoria', y='precio', ax=ax2)
    plt.xticks(rotation=45)
    st.pyplot(fig2)

st.subheader("Matriz de correlación")
fig3, ax3 = plt.subplots()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="Blues", ax=ax3)
st.pyplot(fig3)
