from pymongo import MongoClient

def get_database_connection():
    """Establece conexión con MongoDB"""
    try:
        client = MongoClient('mongodb://localhost:27017/')
        return client
    except Exception as e:
        st.error(f"Error de conexión a MongoDB: {e}")
        return None

def get_collections():
    """Obtiene las colecciones de la base de datos"""
    client = get_database_connection()
    if client:
        db = client['trophycabinet']
        return {
            'trofeos': db['trophies'],
            'estadisticas': db['estadisticas'],
            'equipos': db['equipos_temporada']
        }
    return None