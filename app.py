import streamlit as st
import pandas as pd
import sidetable as stb 
import plotly.express as px

st.title("_Data Analytics Portafolio_de :blue[Flor Borja] :sunglasses:")

st.write('Analisis Exploratorio Inicial:')

raw_data =pd.read_csv('analisis-anuncios-vehiculos/vehicles_us.csv')

st.write('Revisar tipos de datos de las columnas:')
st.dataframe(raw_data.dtypes.rename('datatype'))

st.write('Revisar primeras filas:')
st.dataframe(raw_data.head())

st.write('Revisar primeras filas:')
st.dataframe(raw_data.tail())

st.write('Revisar primeros valores ausentes:')
st.dataframe(raw_data.stb.missing(style=True))

st.write('Revisar filas duplicados:')



