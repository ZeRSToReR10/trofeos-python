import streamlit as st

st.set_page_config(
    page_title="Vitrina de Trofeos",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 Vitrina de Trofeos")
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Trofeos Individuales")
    st.page_link("pages/trofeos_individuales.py", label="Ver trofeos individuales", icon="👤")

with col2:
    st.subheader("Trofeos Colectivos")
    st.page_link("pages/trofeos_colectivos.py", label="Ver trofeos colectivos", icon="👥")

with col3:
    st.subheader("Estadísticas")
    st.page_link("pages/estadisticas.py", label="Ver estadísticas", icon="📊")

with col3:
    st.subheader("Agregar Estadísticas")
    st.page_link("pages/editar_estadisticas.py", label="Agregar estadísticas", icon="✏️")


st.markdown("---")

col5, col6, col7 = st.columns(3)

with col5:
    st.subheader("Agregar Trofeos")
    st.page_link("pages/agregar_trofeos.py", label="Agregar nuevos trofeos", icon="➕")

with col6:
    st.subheader("Configuración")
    st.page_link("pages/configuracion.py", label="Configurar equipos", icon="⚙️")

with col7:
    st.subheader("Resumen")
    st.info("Selecciona una opción del menú para comenzar")