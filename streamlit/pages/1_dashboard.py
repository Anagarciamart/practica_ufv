import pandas as pd

import streamlit as st
import plotly.express as px

import requests
import seaborn as sns


@st.cache_data
def load_data(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    mijson = r.json()
    listado = mijson['libros']
    df = pd.DataFrame.from_records(listado)
    return df


def info_box(texto):
    st.markdown(f'<div style = "background-color:#4EBAE1;opacity:70%"><p style="text-align:center;color:white;font-size:30px;">{texto}</p></div>', unsafe_allow_html=True)


# Llamo a load_data
df_m = load_data('http://fastapi:8000/retrieve_data/')

# Calcular variables
registros = str(df_m.shape[0])
autores_unicos = str(df_m['autor'].nunique())
editoriales_unicas = str(df_m['editorial'].nunique())
rating_promedio_autores = str(round(df_m['autor_rating_promedio'].mean(), 2))
reviews_promedio_libros = str(round(df_m['libro_review_counts'].mean(), 2))

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
    info_box(rating_promedio_autores)
with col5:
    col5.subheader('# Rating Promedio de Reviews')
    info_box(reviews_promedio_libros)

# Agregar una selección para el usuario
seleccion = st.selectbox("Seleccione una opción", ["Información General", "Distribución de Ratings Promedio de Autores", "Pie Chart", "Bar Chart", "Scatter Plot"])

# Mostrar información o gráfico según la selección del usuario
if seleccion == "Distribución de Ratings Promedio de Autores":
    grafico_autores = px.histogram(df_m, x='autor_rating_promedio', title='Distribución de Ratings Promedio de Autores', nbins=20)
    st.plotly_chart(grafico_autores, use_container_width=True)

elif seleccion == "Pie Chart":
    # Gráfico de queso basado en la columna 'pais'
    grafico_pie = px.pie(df_m, names='pais', title='Distribución de Paises', hole=0.3)
    st.plotly_chart(grafico_pie, use_container_width=True)

elif seleccion == "Bar Chart":
    # Gráfico de barras basado en la columna 'autor'
    grafico_barras = px.bar(df_m, x='autor', title='Número de Libros por Autor')
    st.plotly_chart(grafico_barras, use_container_width=True)

elif seleccion == "Scatter Plot":
    # Gráfico de dispersión basado en las columnas 'numpaginas' y 'autor_rating_promedio'
    grafico_dispersion = px.scatter(df_m, x='numpaginas', y='autor_rating_promedio', title='Scatter Plot: Número de Páginas vs Rating Promedio de Autores')
    st.plotly_chart(grafico_dispersion, use_container_width=True)
