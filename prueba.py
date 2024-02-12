import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium 
# Crear datos de ejemplo
datos = pd.DataFrame({
    'Fecha': pd.date_range(start='2022-01-01', periods=100),
    'CO': np.random.rand(100) * 100,
    'CO2': np.random.rand(100) * 100,
    'PM2.5': np.random.rand(100) * 100,
    'LAT': np.random.rand(100) * 100,
    'LON' : np.random.rand(100) * 100

})

# Configurar la barra lateral
pagina = st.sidebar.selectbox("Página", ["CO", "CO2","PM2.5"])

# Función para visualización
def CO():
    st.title("Visualización de Datos - CO")
    st.write("Encontradas datos actualizados sobre la emisión de CO")
    st.header("Tabla de Datos")
    st.dataframe(datos[['Fecha','CO']])

    # Gráfico de línea para CO
    st.subheader("CO")
    plt.plot(datos['Fecha'], datos['CO'])
    plt.xlabel('Fecha')
    plt.ylabel('CO')
    st.pyplot(plt)

    st.header("Mapa geográfico")

    st.map(datos[['LAT','LON']])
     
    



    

# Función para tabla
def CO2():
    st.title("Visualización de Datos - CO2")
    st.write("Encontradas datos actualizados sobre la emisión de CO2")
    st.header("Tabla de Datos")
    st.dataframe(datos[['Fecha','CO2']])

    # Gráfico de línea para CO2
    st.subheader("CO2")
    plt.plot(datos['Fecha'], datos['CO2'])
    plt.xlabel('Fecha')
    plt.ylabel('CO2')
    st.pyplot(plt)

    st.header("Mapa geográfico")

    st.map(datos[['LAT','LON']])

def PM():
    st.title("Visualización de Datos - PM2.5")
    st.write("Encontradas datos actualizados sobre la emisión de particulas finas PM 2.5")

    st.header("Tabla de Datos")
    st.dataframe(datos[['Fecha','PM2.5']])


    # Gráfico de línea para PM2.5
    st.subheader("PM2.5")
    plt.plot(datos['Fecha'], datos['PM2.5'])
    plt.xlabel('Fecha')
    plt.ylabel('PM2.5')
    st.pyplot(plt)

    st.header("Mapa geográfico")

    st.map(datos[['LAT','LON']])

# Mostrar página seleccionada
if pagina == "CO":
    CO()
elif pagina == "CO2":
    CO2()

elif pagina == "PM2.5":
    PM()
