import streamlit as st
from modules.database import get_collections
from modules.constants import MAPEO_IMAGENES, TEMPORADAS_DISPONIBLES
import os

st.set_page_config(page_title="Trofeos Individuales", page_icon="👤")

st.title("👤 Trofeos Individuales")

# Obtener datos de MongoDB
collections = get_collections()
if collections:
    trofeos = collections['trofeos']
    equipos = collections['equipos']
    
    # Filtros
    col1, col2 = st.columns(2)
    with col1:
        temporada_seleccionada = st.selectbox("Filtrar por temporada:", ["Todas"] + TEMPORADAS_DISPONIBLES)
    
    with col2:
        # Obtener tipos de trofeos individuales únicos
        tipos_trofeos = trofeos.distinct("nombre", {"tipo": "Individual"})
        trofeo_seleccionado = st.selectbox("Filtrar por trofeo:", ["Todos"] + tipos_trofeos)
    
    # Construir query
    query = {"tipo": "Individual"}
    if temporada_seleccionada != "Todas":
        query["temporada"] = temporada_seleccionada
    if trofeo_seleccionado != "Todos":
        query["nombre"] = trofeo_seleccionado
    
    # Obtener trofeos
    trofeos_data = list(trofeos.find(query))
    
    if trofeos_data:
        # Agrupar por temporada
        temporadas = {}
        for trofeo in trofeos_data:
            temp = trofeo.get("temporada", "Desconocida")
            if temp not in temporadas:
                temporadas[temp] = []
            temporadas[temp].append(trofeo)
        
        # Mostrar trofeos
        for temporada, trofeos_temp in sorted(temporadas.items()):
            # Obtener equipo de esta temporada
            equipo_doc = equipos.find_one({"temporada": temporada})
            nombre_equipo = f" - {equipo_doc['equipo']}" if equipo_doc else ""
            
            st.subheader(f"Temporada {temporada}{nombre_equipo}")
            
            # Mostrar trofeos en columnas
            cols = st.columns(3)
            for i, trofeo in enumerate(trofeos_temp):
                with cols[i % 3]:
                    nombre = trofeo.get("nombre", "")
                    goles = trofeo.get("goles", 0)
                    asistencias = trofeo.get("asistencias", 0)
                    
                    # Intentar cargar imagen
                    ruta_img = None
                    if nombre in MAPEO_IMAGENES:
                        # Ajusta esta ruta según tu estructura de archivos
                        ruta_img = f"images/{MAPEO_IMAGENES[nombre]}"
                    
                    if ruta_img and os.path.exists(ruta_img):
                        st.image(ruta_img, width=200)
                    
                    st.write(f"**{nombre}**")
                    if "Máximo Goleador" in nombre:
                        st.write(f"Goles: {goles}")
                    elif "Máximo Asistente" in nombre:
                        st.write(f"Asistencias: {asistencias}")
                    else:
                        st.write(f"Goles: {goles}")
                        st.write(f"Asistencias: {asistencias}")
                    
                    st.markdown("---")
    else:
        st.info("No se encontraron trofeos individuales con los filtros seleccionados")
else:
    st.error("No se pudo conectar a la base de datos")