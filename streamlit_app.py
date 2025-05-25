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

st.subheader("1. Primeros registros")
st.write(df.head())

st.subheader("2. Mostrar un grupo de filas (de la 10 a la 20)")
st.write(df.iloc[10:21])

st.subheader("3. Mostrar un grupo de columnas (marca y precio)")
st.write(df[['marca', 'precio']].head(10))

st.subheader("4. Estructura del dataset")
st.write("Dimensiones:", df.shape)
st.write("Columnas y tipos de datos:")
st.write(df.dtypes)

st.subheader("5. Datos únicos por columna")
st.write(df.nunique())



st.subheader("6. Valores nulos")
st.write(df.isnull().sum())

st.subheader("7. Estadísticas Descriptivas (Precio)")

# Convertir a DataFrame y reiniciar índice
stats_df = df['precio'].describe().reset_index()

# Renombrar columnas para mayor claridad
stats_df.columns = ['Estadística', 'Valor']

# Mostrar el DataFrame con nombres explícitos
st.write(stats_df)

st.write("Moda del precio:", df['precio'].mode()[0])
st.write("Mediana del precio:", df['precio'].median())

st.subheader("8. Histograma de precios")

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


st.subheader("9. Diagrama de caja (Boxplot) por categoría")
fig2, ax2 = plt.subplots()
sns.boxplot(data=df, x='categoria', y='precio', ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

st.subheader("10. Diagrama de barras por cantidad de productos por categoría")

# Contar la cantidad de productos por categoría
categoria_count = df['categoria'].value_counts()

# Crear figura y eje
fig4, ax4 = plt.subplots(figsize=(8, 5))
sns.barplot(x=categoria_count.index, y=categoria_count.values, ax=ax4, palette="Set2")

# Etiquetas y rotación
ax4.set_xlabel("Categoría")
ax4.set_ylabel("Cantidad de productos")
ax4.set_title("Cantidad de productos por categoría")
ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45)

# Mostrar gráfico en Streamlit
st.pyplot(fig4)

st.subheader("11. Diagrama de barras por precio promedio por categoría")

# Agrupar por categoría y calcular promedio de precio
categoria_precio_prom = df.groupby('categoria')['precio'].mean().sort_values(ascending=False)

# Crear figura y eje
fig5, ax5 = plt.subplots(figsize=(8, 5))
sns.barplot(x=categoria_precio_prom.index, y=categoria_precio_prom.values, ax=ax5, palette="Set3")

# Etiquetas y título
ax5.set_xlabel("Categoría")
ax5.set_ylabel("Precio promedio")
ax5.set_title("Precio promedio por categoría")
ax5.set_xticklabels(ax5.get_xticklabels(), rotation=45)

# Mostrar gráfico en Streamlit
st.pyplot(fig5)


st.subheader("12. Diagrama de torta por categoría")
fig4, ax4 = plt.subplots()
df['categoria'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax4)
ax4.set_ylabel('')
st.pyplot(fig4)

st.subheader("13. Análisis Bivariado: Precio por Categoría")
fig5, ax5 = plt.subplots()
sns.barplot(data=df, x='categoria', y='precio', estimator='mean', ax=ax5)
ax5.set_xticklabels(ax5.get_xticklabels(), rotation=45)
st.pyplot(fig5)

st.subheader("14. 📊 Tabla de Frecuencia Absoluta y Relativa - Columna 'marca'")

# Verificar si la columna existe
if 'marca' in df.columns:
    # Calcular frecuencias
    frecuencia_abs = df['marca'].value_counts()
    frecuencia_rel = df['marca'].value_counts(normalize=True).round(4) * 100  # porcentaje

    # Unir en un solo DataFrame
    tabla_frecuencia = pd.DataFrame({
        'Frecuencia Absoluta': frecuencia_abs,
        'Frecuencia Relativa (%)': frecuencia_rel
    })

    # Mostrar la tabla
    st.write(tabla_frecuencia)
else:
    st.warning("La columna 'marca' no existe en el DataFrame.")

