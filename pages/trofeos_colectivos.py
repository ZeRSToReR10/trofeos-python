import streamlit as st
from modules.database import get_collections
from modules.constants import MAPEO_IMAGENES, TEMPORADAS_DISPONIBLES
import os

st.set_page_config(page_title="Trofeos Colectivos", page_icon="👥")

st.title("👥 Trofeos Colectivos")

collections = get_collections()
if collections:
    trofeos_collection = collections['trofeos']
    equipos_collection = collections['equipos']
    
    col1, col2 = st.columns(2)
    with col1:
        temporada_seleccionada = st.selectbox("Filtrar por temporada:", ["Todas"] + TEMPORADAS_DISPONIBLES)
    
    with col2:
        tipos_trofeos = trofeos_collection.distinct("nombre", {"tipo": "Colectivo"})
        trofeo_seleccionado = st.selectbox("Filtrar por trofeo:", ["Todos"] + tipos_trofeos)
    
    query = {"tipo": "Colectivo"}
    if temporada_seleccionada != "Todas":
        query["temporada"] = temporada_seleccionada
    if trofeo_seleccionado != "Todos":
        query["nombre"] = trofeo_seleccionado
    
    trofeos_data = list(trofeos_collection.find(query))
    
    if trofeos_data:
        temporadas = {}
        for trofeo in trofeos_data:
            temp = trofeo.get("temporada", "Desconocida")
            if temp not in temporadas:
                temporadas[temp] = []
            temporadas[temp].append(trofeo)
        
        for temporada, trofeos_temp in sorted(temporadas.items()):
            equipo_doc = equipos_collection.find_one({"temporada": temporada})
            nombre_equipo = f" - {equipo_doc['equipo']}" if equipo_doc else ""
            
            st.subheader(f"Temporada {temporada}{nombre_equipo}")
            
            cols = st.columns(3)
            for i, trofeo in enumerate(trofeos_temp):
                with cols[i % 3]:
                    nombre = trofeo.get("nombre", "")
                    goles = trofeo.get("goles", 0)
                    asistencias = trofeo.get("asistencias", 0)
                    
                    ruta_img = None
                    if nombre in MAPEO_IMAGENES:
                        ruta_img = f"imagenes_trofeos/{MAPEO_IMAGENES[nombre]}"
                    
                    if ruta_img and os.path.exists(ruta_img):
                        st.image(ruta_img, width=200)
                    
                    st.write(f"**{nombre}**")
                    st.write(f"Goles: {goles}")
                    st.write(f"Asistencias: {asistencias}")
                    
                    st.markdown("---")
    else:
        st.info("No se encontraron trofeos colectivos con los filtros seleccionados")
else:
    st.error("No se pudo conectar a la base de datos")
