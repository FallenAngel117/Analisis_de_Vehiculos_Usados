import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Título principal de la aplicación
st.header('Análisis de Anuncios de Vehículos Usados')

# Descripción opcional
st.write("Esta aplicación permite visualizar los datos de vehículos usados disponibles para la venta en EE. UU.")

# Botón para construir histograma
hist_button = st.button('Construir histograma del odómetro')

if hist_button:
    st.write('Creación de un histograma para la columna "odometer"')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión (año vs precio)')

if scatter_button:
    st.write('Creación de gráfico de dispersión: modelo por año vs precio')
    fig_scatter = px.scatter(car_data, x="model_year", y="price", color="type")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Opcional: versión con checkboxes
st.markdown("### Opcional: Visualizaciones con casillas de verificación")

# Checkbox para histograma
if st.checkbox('Mostrar histograma (checkbox)'):
    st.write('Histograma de odómetro')
    fig_hist_cb = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist_cb, use_container_width=True)

# Checkbox para dispersión
if st.checkbox('Mostrar gráfico de dispersión (checkbox)'):
    st.write('Gráfico de dispersión de modelo por año vs precio')
    fig_scatter_cb = px.scatter(car_data, x="model_year", y="price", color="type")
    st.plotly_chart(fig_scatter_cb, use_container_width=True)
