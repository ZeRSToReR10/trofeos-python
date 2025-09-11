import streamlit as st
from modules.database import get_collections
from modules.constants import CATEGORIAS_INDIVIDUALES as categorias_individuales
from modules.constants import TEMPORADAS_DISPONIBLES as temporadas_disponibles
from modules.constants import EQUIPOS_DISPONIBLES as equipos_disponibles


def main():

    collections = get_collections()

    if collections is None:
        st.error("No se pudo conectar a la base de datos")
        st.stop()

    estadisticas = collections["estadisticas"]
    equipos = collections["equipos"]
    trofeos = collections["trofeos"]

    st.title("✏️ Agregar Estadísticas")
    categoria = st.selectbox("📂 Categoría", list(categorias_individuales.keys()))
    
    competencias = categorias_individuales.get(categoria, [])
    competencia = st.selectbox("🏆 Competencia", competencias)

    temporada = st.selectbox("📅 Temporada", [
        "22/23","23/24", "24/25", "25/26", "26/27", "27/28", "28/29",
        "29/30", "30/31", "31/32", "32/33", "33/34", "34/35",
        "35/36", "36/37", "37/38", "38/39", "39/40", "40/41"
    ])

    st.markdown("### 📊 Ingresar Estadísticas")
    col1, col2 = st.columns(2)

    with col1:
        pj = st.number_input("Partidos Jugados", min_value=0, step=1)
        goles = st.number_input("Goles", min_value=0, step=1)
        asist = st.number_input("Asistencias", min_value=0, step=1)

    with col2:
        amarillas = st.number_input("Tarjetas Amarillas", min_value=0, step=1)
        rojas = st.number_input("Tarjetas Rojas", min_value=0, step=1)

    if st.button("💾 Guardar Estadísticas"):
        filtro = {"competencia": competencia, "temporada": temporada}
        existente = estadisticas.find_one(filtro)

        if existente:
            nueva_data = {
                "partidos": existente.get("partidos", 0) + pj,
                "goles": existente.get("goles", 0) + goles,
                "asistencias": existente.get("asistencias", 0) + asist,
                "amarillas": existente.get("amarillas", 0) + amarillas,
                "rojas": existente.get("rojas", 0) + rojas,
            }
            estadisticas.update_one(filtro, {"$set": nueva_data})
            st.success("✅ Estadísticas actualizadas correctamente.")
        else:
            nueva_data = {
                "competencia": competencia,
                "temporada": temporada,
                "partidos": pj,
                "goles": goles,
                "asistencias": asist,
                "amarillas": amarillas,
                "rojas": rojas
            }
            estadisticas.insert_one(nueva_data)
            st.success("✅ Nueva estadística creada correctamente.")

if __name__ == "__main__":
    main()
