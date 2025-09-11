# Vitrina de Trofeos – Modo Carrera

Esta aplicación en Python permite gestionar, visualizar y editar trofeos y estadísticas de jugadores y equipos en modo carrera de FIFA / FC. Utiliza MongoDB como base de datos y Streamlit para la interfaz web.

### Pre-requisitos 📋
```
Python 3.7 o superior
MongoDB corriendo localmente
```

## 📂 Estructura del proyecto
```
trofeos-python/
│
├── modules/ # Conexion a base de datos y constantes
├── pages/ # Páginas (Trofeos individuales, colectivos, estadísticas, agregar trofeos)
├── images/ # Imágenes de trofeos y equipos
├── Home.py # Página principal
├── requirements.txt # Dependencias del proyecto
```
### Instalación 🔧

1. Clona el repositorio:
```
git clone git@github.com:tu_usuario/trofeos-python.git
cd trofeos-python
```
2. Crea un entorno virtual e instala dependencias:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```
streamlit run Home.py
```
4. Agrega un trofeo desde la interfaz y verifica que aparece en la base de datos MongoDB en la colección 'trophies'.


## Personalización 🎨

Todas las imágenes de trofeos y equipos se encuentran en images/.

Puedes modificar el mapeo de imágenes y temporadas en modules/constants.py.

Las categorías y competencias están definidas también en modules/constants.py.

## Construido con 🛠️

* [Python](https://www.python.org/) - Lenguaje principal
* [MongoDB](https://www.mongodb.com/) - Base de datos
* [Streamlit](https://streamlit.io/) - Interfaz web
* [Pymongo](https://pymongo.readthedocs.io/) - Conexión a MongoDB desde Python




