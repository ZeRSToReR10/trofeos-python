import streamlit as st
from pymongo import MongoClient
from modules.database import get_collections
from modules.constants import CATEGORIAS_INDIVIDUALES as categorias_individuales
from modules.constants import TEMPORADAS_DISPONIBLES as temporadas_disponibles

collections = get_collections()

if collections is None:
    st.error("No se pudo conectar a la base de datos")
    st.stop()

estadisticas = collections["estadisticas"]
equipos = collections["equipos"]
trofeos = collections["trofeos"]

categorias_colectivas = categorias_individuales

opciones_individuales = [
    "Balón de oro",
    "Bota de oro",
    "Máximo Goleador",
    "Máximo Asistente",
    "Mejor Jugador",
    "Jugador UEFA",
    "Jugador CONMEBOL"
]
opciones_colectivos = ["Torneo Ganado"]

# ----------------- UI -----------------
st.title("➕ Agregar Trofeo")

tipo_preset = st.radio("Tipo de Trofeo", ["Individual", "Colectivo"], horizontal=True)

# Selección de nombre base
opciones_nombre = opciones_individuales if tipo_preset == "Individual" else opciones_colectivos
nombre_base = st.selectbox("🏅 Nombre del Trofeo", opciones_nombre)

# Mostrar categoría y competencia solo cuando corresponda
competencia = ""
if tipo_preset == "Colectivo" or nombre_base in ["Máximo Goleador", "Máximo Asistente", "Mejor Jugador"]:
    categoria = st.selectbox("📂 Categoría", list(categorias_individuales.keys()))
    competencia = st.selectbox("⚽ Competencia", categorias_individuales[categoria])
else:
    categoria = None

# Temporada
temporada = st.selectbox("📅 Temporada", temporadas_disponibles)

# Campos de goles y asistencias
goles = 0
asistencias = 0
if tipo_preset == "Colectivo":
    goles = st.number_input("⚽ Goles", min_value=0, step=1)
    asistencias = st.number_input("🎯 Asistencias", min_value=0, step=1)
elif nombre_base == "Máximo Goleador":
    goles = st.number_input("⚽ Goles", min_value=0, step=1)
elif nombre_base == "Máximo Asistente":
    asistencias = st.number_input("🎯 Asistencias", min_value=0, step=1)

# ----------------- Guardar -----------------
if st.button("💾 Guardar Trofeo"):
    # Construcción del nombre y ámbito
    nombre = nombre_base
    ambito = "local"

    if tipo_preset == "Colectivo":
        nombre = competencia
    elif tipo_preset == "Individual" and nombre_base in ["Máximo Goleador", "Máximo Asistente", "Mejor Jugador"] and competencia:
        nombre += f" {competencia}"
        if any(word in competencia.lower() for word in ["champions", "europa", "conference", "libertadores", "world", "uefa", "copa américa"]):
            ambito = "internacional"
    elif nombre_base.lower() in ["balón de oro", "bota de oro", "jugador uefa"]:
        ambito = "internacional"

    if tipo_preset == "Colectivo" and any(nombre.lower() in c.lower() for cat in categorias_colectivas.values() for c in cat if any(word in c.lower() for word in ["champions", "libertadores", "world", "intercontinental", "euro", "copa américa"])):
        ambito = "internacional"

    trofeo = {
        "nombre": nombre,
        "temporada": temporada,
        "goles": goles,
        "asistencias": asistencias,
        "tipo": tipo_preset,
        "ambito": ambito,
    }

    trofeos.insert_one(trofeo)
    st.success(f"🏆 Trofeo '{nombre}' agregado correctamente.")
