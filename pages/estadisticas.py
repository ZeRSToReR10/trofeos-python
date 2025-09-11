import streamlit as st
from pymongo import MongoClient
from modules.database import get_collections
import pandas as pd
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_IMAGENES = BASE_DIR.parent / "equipos"

def main():
    collections = get_collections()

    if collections is None:
        st.error("No se pudo conectar a la base de datos")
        st.stop()

    estadisticas = collections["estadisticas"]
    equipos = collections["equipos"]

    datos = list(estadisticas.find())
    if not datos:
        st.warning("⚠️ No hay estadísticas guardadas en la base de datos todavía.")
        return

    # Agrupar por temporada
    agrupado = {}
    for est in datos:
        temp = est.get("temporada", "Desconocida")
        agrupado.setdefault(temp, []).append(est)

    # Ordenar temporadas
    temporadas_ordenadas = sorted(
        agrupado.keys(),
        key=lambda t: t.split("/")[0] if "/" in t else t
    )

    st.title("📊 Estadísticas por Temporada")

    for temp in temporadas_ordenadas:
        equipo_doc = equipos.find_one({"temporada": temp})
        nombre_equipo = equipo_doc["equipo"] if equipo_doc else "Sin equipo"

        # Logo
        ruta_logo = os.path.join(RUTA_IMAGENES, f"{nombre_equipo}.png")

        col1, col2 = st.columns([1, 6])
        with col1:
            if os.path.exists(ruta_logo):
                st.image(ruta_logo, width=40)
        with col2:
            st.subheader(f"📅 Temporada {temp} - {nombre_equipo}")

        # Tabla de estadísticas
        filas = []
        total_partidos = total_goles = total_asistencias = total_amarillas = total_rojas = 0

        for est in agrupado[temp]:
            partidos = est.get("partidos", 0)
            goles = est.get("goles", 0)
            asistencias = est.get("asistencias", 0)
            amarillas = est.get("amarillas", 0)
            rojas = est.get("rojas", 0)

            g_a = goles + asistencias
            g_por_partido = round(goles / partidos, 2) if partidos > 0 else 0.0

            filas.append([
                est.get("competencia", ""),
                partidos, goles, asistencias, g_a, g_por_partido, amarillas, rojas
            ])

            total_partidos += partidos
            total_goles += goles
            total_asistencias += asistencias
            total_amarillas += amarillas
            total_rojas += rojas

        total_g_a = total_goles + total_asistencias
        total_gpp = round(total_goles / total_partidos, 2) if total_partidos > 0 else 0.0

        filas.append([
            "TOTAL", total_partidos, total_goles, total_asistencias,
            total_g_a, total_gpp, total_amarillas, total_rojas
        ])

        columnas = ["Competencia", "Partidos", "Goles", "Asistencias", "G/A", "G/P", "Amarillas", "Rojas"]
        df_temp = pd.DataFrame(filas, columns=columnas)

        st.dataframe(df_temp, use_container_width=True)

if __name__ == "__main__":
    main()
