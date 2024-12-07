import streamlit as st
import pandas as pd
import sidetable as stb 
import plotly.express as px

st.title("_Data Analytics Portafolio_de :blue[Flor Borja] :sunglasses:")

st.write('Analisis Exploratorio Inicial:')

raw_data =pd.read_csv('analisis-anuncios-vehiculos/vehicles_us.csv')

st.write('Revisar primeras filas:')
st.dataframe(raw_data.head())

st.write('Revisar primeras estructuras del dataframes')
st.dataframe(raw_data.info())

st.write('Revisar primeros valores ausentes:')
st.dataframe(raw_data.stb.missing(style=True))

boton_barras = st.button('Crear un grafico de barras sobre fecha de la publicacion', type='primary')

if  boton_barras:
    st.bar_chart(raw_data['date_posted'])

boton_histograma =st.button('Crear grafico de histograma sobre la fecha de publicacion', type='primary')
    
if boton_histograma:
    fig= px.histogram(raw_data, x='date_posted')

    st.plotly_chart(fig)