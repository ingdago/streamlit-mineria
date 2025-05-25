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

st.title("📊 Análisis Exploratorio")

st.subheader("1️⃣ Primeros registros")
st.write(df.head())

st.subheader("2️⃣ Estructura del dataset")
st.write("Dimensiones:", df.shape)
st.write("Columnas y tipos de datos:")
st.write(df.dtypes)

st.subheader("3️⃣ Datos únicos por columna")
st.write(df.nunique())

st.subheader("4️⃣ Valores nulos")
st.write(df.isnull().sum())

st.subheader("5️⃣ Estadísticas Descriptivas (Precio)")

# Convertir a DataFrame y reiniciar índice
stats_df = df['precio'].describe().reset_index()

# Renombrar columnas para mayor claridad
stats_df.columns = ['Estadística', 'Valor']

# Mostrar el DataFrame con nombres explícitos
st.write(stats_df)

st.write("Moda del precio:", df['precio'].mode()[0])
st.write("Mediana del precio:", df['precio'].median())

st.subheader("6️⃣ Histograma de precios")

# Crear figura y eje
fig1, ax1 = plt.subplots(figsize=(10, 5))  # Tamaño más ancho

# Histograma con número de bins personalizado y sin valores extremos
sns.histplot(df['precio'], kde=True, bins=30, ax=ax1)

# Opcional: limitar el eje X para enfocar en los valores comunes (quita valores extremos)
ax1.set_xlim(df['precio'].quantile(0.01), df['precio'].quantile(0.99))  # Quitar outliers

# Título y etiquetas
ax1.set_title("Distribución de precios (sin valores extremos)")
ax1.set_xlabel("Precio")
ax1.set_ylabel("Frecuencia")

# Mostrar en Streamlit
st.pyplot(fig1)


st.subheader("7️⃣ Diagrama de caja (Boxplot) por categoría")
fig2, ax2 = plt.subplots()
sns.boxplot(data=df, x='categoria', y='precio', ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

st.subheader("8️⃣ Diagrama de barras por marca")
marca_count = df['marca'].value_counts()
fig3, ax3 = plt.subplots()
sns.barplot(x=marca_count.index, y=marca_count.values, ax=ax3)
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=90)
st.pyplot(fig3)

st.subheader("9️⃣ Diagrama de torta por categoría")
fig4, ax4 = plt.subplots()
df['categoria'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax4)
ax4.set_ylabel('')
st.pyplot(fig4)

st.subheader("🔄 Análisis Bivariado: Precio por Categoría")
fig5, ax5 = plt.subplots()
sns.barplot(data=df, x='categoria', y='precio', estimator='mean', ax=ax5)
ax5.set_xticklabels(ax5.get_xticklabels(), rotation=45)
st.pyplot(fig5)

st.subheader("🔄 Tabla de contingencia: Categoría vs Marca")
tabla = pd.crosstab(df['categoria'], df['marca'])
st.write(tabla)
