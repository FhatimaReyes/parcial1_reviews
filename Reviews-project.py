import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

#Icon
st.set_page_config(page_title="Reviews • Streamlit", page_icon="icono.png", layout="centered")

#Presentación
st.title('Reviews of Women Clothes')
st.markdown("Base de Datos No Convencionales - 601 ISW")
st.markdown("""Fhatima Reyes Alejandre - S20006773\n
zS20006773@estudiantes.uv.mx""")

#Dataset
DATA_URL = ('reviews_dresses.csv')

#Lectura del dataset
@st.cache_resource
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data
data = load_data(1500)

#Sidebar
st.sidebar.image("logo.png")

#Para mostrar 
if st.sidebar.checkbox('Mostrar datos'):
    st.subheader('Dataset')
    st.write(data)

#buscador 
query = st.sidebar.text_input("Buscar por departamento: ")
query = query.upper()
if st.sidebar.button('Buscar', key='button1'):
    data['department'] = data['department'].dropna()
    data['department'] = data['department'].astype(str)
    results = data[data["department"].str.upper().str.contains(query)]
    st.header('Resultados:')
    st.table(results)

query = st.sidebar.text_input("Buscar por categoría: ")
query = query.upper()
if st.sidebar.button('Buscar', key='button2'):
    # Filtra los datos que contienen la consulta ingresada
    data['class'] = data['class'].dropna()
    data['class'] = data['class'].astype(str)
    results = data[data["class"].str.upper().str.contains(query)]
    # Muestra los resultados
    st.header('Prendas encontradas:')
    st.table(results)

    ##----El buscador de Reviews creado en clase----
query = st.sidebar.text_input("Emotions in Reviews: ")
query = query.upper()
if st.sidebar.button('Buscar', key='button3'):
    # Filtra los datos que contienen la consulta ingresada
    data['reviews'] = data['reviews'].dropna()
    data['reviews'] = data['reviews'].astype(str)
    results = data[data["reviews"].str.upper().str.contains(query)]
    # Muestra los resultados
    st.header('Comentarios encontrados:')
    st.table(results)





 #Multiselect
st.sidebar.markdown("##")
department = st.sidebar.multiselect("Selecciona el departamento:", data["department"].unique(), default=data["department"].unique())
departmentFilter = data[data["department"].isin(department)]

st.sidebar.markdown("##")
division = st.sidebar.multiselect("Selecciona la división de prenda:", data["division"].unique(), default=data["division"].unique())
divisionFilter = data[data["division"].isin(division)]

st.sidebar.markdown("##")
rating = st.sidebar.multiselect("Selecciona el rating:", data["rating"].unique(), default=data["rating"].unique())
ratingFilter = data[data["rating"].isin(rating)] 

#Histograma
fig, ax = plt.subplots()

ax.hist(data['age'], bins=35, edgecolor = "#F5F5F5", color = "#DB7093")
ax.set_title('Histograma de edades de las mujeres')
ax.set_xlabel('Edad')
ax.set_ylabel('Cantidad')
plt.style.use('dark_background')
st.sidebar.markdown("##")
if st.sidebar.checkbox('Mostrar histograma', key="buttonHistogram"):
    st.pyplot(fig)
    st.markdown(
        'Este histograma muestra las edades de los usuarios que adquieren una prenda.')


# Barsgraph
selection = data.query(
    "department == @department & division == @division & rating == @rating")
fig = px.bar(selection, x="stock", y=["division", "department"])
fig.update_xaxes(title='Categorías')
fig.update_yaxes(title='Valores')
if st.sidebar.checkbox('Mostrar gráfica de barras', key="buttonBarsGraph"):
    st.plotly_chart(fig)
    st.markdown(
        """Esta gráfica de barras muestra la disponibilidad de las prendas dependiendo de su area departamental """)

# Scattergraph
avgclass = selection['class']
fig = px.scatter(selection,
                 x=selection['class'].index,
                 y=avgclass,
                 template="plotly_white")
fig.update_xaxes(title='Scatter')
fig.update_yaxes(title='Clothes')
fig.update_layout(plot_bgcolor="rgba(0,0,0,0)")
if st.sidebar.checkbox('Mostrar gráfica scatter', key="buttonScatterGraph"):
    st.plotly_chart(fig)
    st.markdown(
        'Esta gráfica de dispersión muestra la categoría de cada una de las prendas')

