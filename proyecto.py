import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pydeck as pdk

plt.style.use('ggplot')

st.title('Recuento de Géneros por Región')

df = pd.read_excel('OPENDATA_DS_01_AFILIADOS.xlsx')

# Desapilar el DataFrame
conteo_sexos = df.groupby(['REGION', 'SEXO']).size().unstack(fill_value=0)

fig, ax = plt.subplots(figsize=(9, 14))

# Crear un gráfico de barras con colores específicos y agregar una leyenda
conteo_sexos.plot(kind='barh', color={'FEMENINO': 'blue', 'MASCULINO': 'red'}, ax=ax)

plt.title('Recuento de Géneros por Región')
plt.ylabel('Región')
plt.xlabel('Cantidad')

# Agregar una leyenda
plt.legend(['Femenino', 'Masculino'])

st.pyplot(fig)

# Crear una lista de las regiones únicas en el DataFrame
regiones = df['REGION'].unique().tolist()

# Crear un selectbox para seleccionar una región
region_seleccionada = st.selectbox('Selecciona una región', regiones)

# Filtrar el DataFrame para obtener solo los datos de la región seleccionada
df_filtrado = df[df['REGION'] == region_seleccionada]

# Crear un mapa con los datos de la región seleccionada
st.map(df_filtrado)