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

st.title("📊 Análisis Exploratorio de Datos - Papelería")

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
