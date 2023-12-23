import pandas as pd

import streamlit as st
import plotly.express as px

import seaborn as sns
@st.cache_data
def load_data():
    df = pd.read_csv('/home/ana/repositorios/repos/practicafinal/practica_ufv/fastapi/Libros.csv')
    return df

def info_box (texto, color=None):
    st.markdown(f'<div style = "background-color:#4EBAE1;opacity:70%"><p style="text-align:center;color:white;font-size:30px;">{texto}</p></div>', unsafe_allow_html=True)

# Call the load_data function
df = load_data()

# Calcular variables adicionales
registros = str(df.shape[0])
autores_unicos = str(df['autor'].nunique())
editoriales_unicas = str(df['editorial'].nunique())
rating_promedio_autores = str(round(df['autor_rating_promedio'].mean(), 2))
reviews_promedio_libros = str(round(df['libro_review_counts'].mean(),2))

sns.set_palette("pastel")
st.header("Información general de libros y autores")

col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)

with col1:
    col1.subheader('# Libros')
    info_box(registros)
with col2:
    col2.subheader('# Autores')
    info_box(autores_unicos)
with col3:
    col3.subheader('# Editoriales')
    info_box(editoriales_unicas)
with col4:
    col4.subheader('# Rating Promedio de Autores')
    info_box(rating_promedio_autores, col4)
with col5:
    col5.subheader('# Rating Promedio de Reviews')
    info_box(reviews_promedio_libros, col5)

# Agregar una selección para el usuario
seleccion = st.selectbox("Seleccione una opción", ["Información General", "Distribución de Ratings Promedio de Autores", "Pie Chart", "Bar Chart", "Scatter Plot"])

# Mostrar información o gráfico según la selección del usuario
if seleccion == "Distribución de Ratings Promedio de Autores":
    grafico_autores = px.histogram(df, x='autor_rating_promedio', title='Distribución de Ratings Promedio de Autores', nbins=20)
    st.plotly_chart(grafico_autores, theme="streamlit", use_container_width=True)

elif seleccion == "Pie Chart":
    # Gráfico de queso basado en la columna 'pais'
    grafico_pie = px.pie(df, names='pais', title='Distribución de Paises', hole=0.3)
    st.plotly_chart(grafico_pie, theme="streamlit", use_container_width=True)

elif seleccion == "Bar Chart":
    # Gráfico de barras basado en la columna 'autor'
    grafico_barras = px.bar(df, x='autor', title='Número de Libros por Autor')
    st.plotly_chart(grafico_barras, theme="streamlit", use_container_width=True)

elif seleccion == "Scatter Plot":
    # Crear un gráfico de dispersión basado en las columnas 'numpaginas' y 'autor_rating_promedio'
    grafico_dispersion = px.scatter(df, x='numpaginas', y='autor_rating_promedio', title='Scatter Plot: Número de Páginas vs Rating Promedio de Autores')
    st.plotly_chart(grafico_dispersion, theme="streamlit", use_container_width=True)

