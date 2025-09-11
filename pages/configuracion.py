import streamlit as st
from modules.database import get_collections
from modules.constants import CATEGORIAS_INDIVIDUALES as categorias_individuales
from modules.constants import TEMPORADAS_DISPONIBLES as temporadas_disponibles
from modules.constants import EQUIPOS_DISPONIBLES as equipos_disponibles

st.set_page_config(page_title="Configuración", page_icon="⚙️")

st.title("⚙️ Configuración - Equipos por Temporada")

collections = get_collections()
if collections:
    equipos_collection = collections['equipos']

    with st.form("equipo_temporada_form"):
        temporada = st.selectbox("Temporada", temporadas_disponibles)
        equipo = st.selectbox("Equipo", equipos_disponibles)

        submitted = st.form_submit_button("Guardar")

        if submitted:
            existente = equipos_collection.find_one({"temporada": temporada})
            if existente:
                equipos_collection.update_one({"temporada": temporada}, {"$set": {"equipo": equipo}})
                st.success(f"Actualizado: Temporada {temporada} ahora es {equipo}")
            else:
                equipos_collection.insert_one({"temporada": temporada, "equipo": equipo})
                st.success(f"Agregado: Temporada {temporada} - {equipo}")

    st.subheader("Equipos por Temporada")
    equipos_data = list(equipos_collection.find().sort("temporada", 1))
    if equipos_data:
        for e in equipos_data:
            st.write(f"{e['temporada']}: {e['equipo']}")
    else:
        st.info("No hay equipos configurados.")

else:
    st.error("Error de conexión a la base de datos")