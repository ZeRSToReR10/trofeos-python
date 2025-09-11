import tkinter as tk
from tkinter import ttk, messagebox, Menu
from pymongo import MongoClient
from PIL import Image, ImageTk
import os
from tabulate import tabulate

client = MongoClient('mongodb://localhost:27017/')
db = client['trophycabinet']
trofeos = db['trophies']
estadisticas = db['estadisticas']
ruta_imagenes = "C:\\Users\\GAMING\\Desktop\\Proyectos\\trofeos python\\imagenes_trofeos"


def ventana_ver_trofeos(tipo_filtro):
    import tkinter as tk
    from tkinter import ttk
    from PIL import Image, ImageTk
    import os
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017/")
    db = client["trophycabinet"]
    equipos = db["equipos_temporada"]
    # Carpeta donde están tus imágenes
    RUTA_IMAGENES = "C:\\Users\\GAMING\\Desktop\\Proyectos\\trofeos python\\imagenes_trofeos"

    MAPEO_IMAGENES = {
        "Balón de oro": "balon_de_oro.png",
        "Bota de oro": "bota_de_oro.png",
        "Jugador UEFA": "jugador_uefa.png",

        "Máximo Goleador UEFA Champions League": "champions_league_logo.png",
        "Máximo Asistente UEFA Champions League": "champions_league_logo.png",
        "Mejor Jugador UEFA Champions League": "champions_league_logo.png",

        "Máximo Goleador Intercontinental": "intercontinental.png",
        "Máximo Asistente Intercontinental": "intercontinental.png",
        "Mejor Jugador Intercontinental": "intercontinental.png",

        "Máximo Goleador UEFA Europa League": "europa_league_logo.png",
        "Máximo Asistente UEFA Europa League": "europa_league_logo.png",
        "Mejor Jugador UEFA Europa League": "europa_league_logo.png",

        "Máximo Goleador UEFA Conference League": "conference_league_logo.png",
        "Máximo Asistente UEFA Conference League": "conference_league_logo.png",
        "Mejor Jugador UEFA Conference League": "conference_league_logo.png",

        "Máximo Goleador UEFA Eurocopa": "uefa_euro_logo.png",
        "Máximo Asistente UEFA Eurocopa": "uefa_euro_logo.png",
        "Mejor Jugador UEFA Eurocopa": "uefa_euro_logo.png",

        "Máximo Goleador UEFA SuperCup": "supercup.png",
        "Máximo Asistente UEFA SuperCup": "supercup.png",
        "Mejor Jugador UEFA SuperCup": "supercup.png",

        "Máximo Goleador CONMEBOL Libertadores": "libertadores_logo.png",
        "Máximo Asistente CONMEBOL Libertadores": "libertadores_logo.png",
        "Mejor Jugador CONMEBOL Libertadores": "libertadores_logo.png",

        "Máximo Goleador CONMEBOL Sudamericana": "sudamericana_logo.png",
        "Máximo Asistente CONMEBOL Sudamericana": "sudamericana_logo.png",
        "Mejor Jugador CONMEBOL Sudamericana": "sudamericana_logo.png",

        "Máximo Goleador CONMEBOL Copa América": "copa_america_logo.png",
        "Máximo Asistente CONMEBOL Copa América": "copa_america_logo.png",
        "Mejor Jugador CONMEBOL Copa América": "copa_america_logo.png",

        "Máximo Goleador FIFA World Cup": "fifa_world_cup_logo.png",
        "Máximo Asistente FIFA World Cup": "fifa_world_cup_logo.png",
        "Mejor Jugador FIFA World Cup": "fifa_world_cup_logo.png",

        "Máximo Goleador FIFA Club World Cup": "fifa_club_world_cup_logo.png",
        "Máximo Asistente FIFA Club World Cup": "fifa_club_world_cup_logo.png",
        "Mejor Jugador FIFA Club World Cup": "fifa_club_world_cup_logo.png",

        "Máximo Goleador Premier League (Inglaterra)": "premier_league_logo.png",
        "Máximo Asistente Premier League (Inglaterra)": "premier_league_logo.png",
        "Mejor Jugador Premier League (Inglaterra)": "premier_league_logo.png",

        "Máximo Goleador LaLiga EA Sports (España)": "laliga_logo.png",
        "Máximo Asistente LaLiga EA Sports (España)": "laliga_logo.png",
        "Mejor Jugador LaLiga EA Sports (España)": "laliga_logo.png",

        "Máximo Goleador Serie A TIM (Italia)": "serie_a_logo.png",
        "Máximo Asistente Serie A TIM (Italia)": "serie_a_logo.png",
        "Mejor Jugador Serie A TIM (Italia)": "serie_a_logo.png",

        "Máximo Goleador Bundesliga (Alemania)": "bundesliga_logo.png",
        "Máximo Asistente Bundesliga (Alemania)": "bundesliga_logo.png",
        "Mejor Jugador Bundesliga (Alemania)": "bundesliga_logo.png",

        "Máximo Goleador Ligue 1 Uber Eats (Francia)": "ligue1_logo.png",
        "Máximo Asistente Ligue 1 Uber Eats (Francia)": "ligue1_logo.png",
        "Mejor Jugador Ligue 1 Uber Eats (Francia)": "ligue1_logo.png",

        "Máximo Goleador Eredivise (Holanda)": "eredivise.png",
        "Máximo Asistente Eredivise (Holanda)": "eredivise.png",
        "Mejor Jugador Eredivise (Holanda)": "eredivise.png",

        "Máximo Goleador Campeonato Nacional (Chile)": "campeonato_nacional_chile_logo.png",
        "Máximo Asistente Campeonato Nacional (Chile)": "campeonato_nacional_chile_logo.png",
        "Mejor Jugador Campeonato Nacional (Chile)": "campeonato_nacional_chile_logo.png",

        "Máximo Goleador Liga de Ascenso Caixun (Chile)": "campeonato_nacional_ascenso.png",
        "Máximo Asistente Liga de Ascenso Caixun (Chile)": "campeonato_nacional_ascenso.png",
        "Mejor Jugador Liga de Ascenso Caixun (Chile)": "campeonato_nacional_ascenso.png",

        "Máximo Goleador Copa Coca-Cola Zero (Chile)": "copa_chile.png",
        "Máximo Asistente Copa Coca-Cola Zero (Chile)": "copa_chile.png",
        "Mejor Jugador Copa Coca-Cola Zero (Chile)": "copa_chile.png",

        "Máximo Goleador Liga Profesional de Fútbol Apertura (Argentina)": "liga_profesional_argentina_logo.png",
        "Máximo Asistente Liga Profesional de Fútbol Apertura (Argentina)": "liga_profesional_argentina_logo.png",
        "Mejor Jugador Liga Profesional de Fútbol Apertura (Argentina)": "liga_profesional_argentina_logo.png",

        "Máximo Goleador Liga Profesional de Fútbol Clausura (Argentina)": "liga_profesional_argentina_logo.png",
        "Máximo Asistente Liga Profesional de Fútbol Clausura (Argentina)": "liga_profesional_argentina_logo.png",
        "Mejor Jugador Liga Profesional de Fútbol Clausura (Argentina)": "liga_profesional_argentina_logo.png",

        "Máximo Goleador Primera B Nacional (Argentina)": "primera_b_nacional.png.png",
        "Máximo Asistente Primera B Nacional (Argentina)": "primera_b_nacional.png.png",
        "Mejor Jugador Primera B Nacional (Argentina)": "primera_b_nacional.png.png",

        "Máximo Goleador Campeonato Brasileiro Série A (Brasil)": "serie_a_brasil_logo.png",
        "Máximo Asistente Campeonato Brasileiro Série A (Brasil)": "serie_a_brasil_logo.png",
        "Mejor Jugador Campeonato Brasileiro Série A (Brasil)": "serie_a_brasil_logo.png",

        "Máximo Goleador Copa del Rey (España)": "copa_del_rey_logo.png",
        "Máximo Asistente Copa del Rey (España)": "copa_del_rey_logo.png",
        "Mejor Jugador Copa del Rey (España)": "copa_del_rey_logo.png",

        "Máximo Goleador FA Cup (Inglaterra)": "fa_cup_logo.png",
        "Máximo Asistente FA Cup (Inglaterra)": "fa_cup_logo.png",
        "Mejor Jugador FA Cup (Inglaterra)": "fa_cup_logo.png",

        "Máximo Goleador Carabao Cup (Inglaterra)": "carabao_cup_logo.png",
        "Máximo Asistente Carabao Cup (Inglaterra)": "carabao_cup_logo.png",
        "Mejor Jugador Carabao Cup (Inglaterra)": "carabao_cup_logo.png",

        "Máximo Goleador Coppa Italia (Italia)": "coppa_italia_logo.png",
        "Máximo Asistente Coppa Italia (Italia)": "coppa_italia_logo.png",
        "Mejor Jugador Coppa Italia (Italia)": "coppa_italia_logo.png",

        "Máximo Goleador DFB-Pokal (Alemania)": "dfb_pokal_logo.png",
        "Máximo Asistente DFB-Pokal (Alemania)": "dfb_pokal_logo.png",
        "Mejor Jugador DFB-Pokal (Alemania)": "dfb_pokal_logo.png",

        "Máximo Goleador Coupe de France (Francia)": "coupe_de_france_logo.png",
        "Máximo Asistente Coupe de France (Francia)": "coupe_de_france_logo.png",
        "Mejor Jugador Coupe de France (Francia)": "coupe_de_france_logo.png",

        "Máximo Goleador Supercopa de España (España)": "supercopa_espana_logo.png",
        "Máximo Asistente Supercopa de España (España)": "supercopa_espana_logo.png",
        "Mejor Jugador Supercopa de España (España)": "supercopa_espana_logo.png",

        "Máximo Goleador Community Shield (Inglaterra)": "community_shield_logo.png",
        "Máximo Asistente Community Shield (Inglaterra)": "community_shield_logo.png",
        "Mejor Jugador Community Shield (Inglaterra)": "community_shield_logo.png",

        "Máximo Goleador Supercoppa di Lega (Italia)": "supercoppa_italia_logo.png",
        "Máximo Asistente Supercoppa di Lega (Italia)": "supercoppa_italia_logo.png",
        "Mejor Jugador Supercoppa di Lega (Italia)": "supercoppa_italia_logo.png",

        "Máximo Goleador DFL-Supercup (Alemania)": "dfl_supercup_logo.png",
        "Máximo Asistente DFL-Supercup (Alemania)": "dfl_supercup_logo.png",
        "Mejor Jugador DFL-Supercup (Alemania)": "dfl_supercup_logo.png",

        "Máximo Goleador Trofeo de Campeones (Francia)": "trofeo_campeones_francia_logo.png",
        "Máximo Asistente Trofeo de Campeones (Francia)": "trofeo_campeones_francia_logo.png",
        "Mejor Jugador Trofeo de Campeones (Francia)": "trofeo_campeones_francia_logo.png",

        "Máximo Goleador Supercopa Johan Cruyff (Holanda)": "supercopa_johan_cruyff_logo.png",
        "Máximo Asistente Supercopa Johan Cruyff (Holanda)": "supercopa_johan_cruyff_logo.png",
        "Mejor Jugador Supercopa Johan Cruyff (Holanda)": "supercopa_johan_cruyff_logo.png",

        "UEFA Champions League": "champions_cup.png",
        "Intercontinental": "intercontinental_cup.png",
        "UEFA Europa League": "europa_league_cup.png",
        "UEFA Conference League": "conference_cup.png",
        "UEFA Eurocopa": "euro_cup.png",
        "UEFA SuperCup": "supercup_cup.png",
        "CONMEBOL Libertadores": "libertadores_cup.png",
        "CONMEBOL Sudamericana": "sudamericana_cup.png",
        "CONMEBOL Copa América": "copa_america_cup.png",
        "FIFA World Cup": "fifa_world_cup_cup.png",
        "FIFA Club World Cup": "fifa_club_world_cup_cup.png",
        "Premier League (Inglaterra)": "premier_league_cup.png",
        "LaLiga EA Sports (España)": "laliga_cup.png",
        "Serie A TIM (Italia)": "serie_a_cup.png",
        "Bundesliga (Alemania)": "bundesliga_cup.png",
        "Ligue 1 Uber Eats (Francia)": "ligue1_cup.png",
        "Campeonato Nacional (Chile)": "campeonato_nacional_chile_cup.png",
        "Liga Profesional de Fútbol Apertura (Argentina)": "liga_profesional_argentina_cup.png",
        "Liga Profesional de Fútbol Clausura (Argentina)": "liga_profesional_argentina_cup.png",
        "Campeonato Brasileiro Série A (Brasil)": "serie_a_brasil_cup.png",
        "Copa del Rey (España)": "copa_del_rey_cup.png",
        "FA Cup (Inglaterra)": "fa_cup_cup.png",
        "Coppa Italia (Italia)": "coppa_italia_cup.png",
        "DFB-Pokal (Alemania)": "dfb_pokal_cup.png",
        "Coupe de France (Francia)": "coupe_de_france_cup.png",
        "CONMEBOL Recopa": "CONMEBOL_recopa.png",

        "Supercopa de España (España)": "supercopa_espana_cup.png",
        "Community Shield (Inglaterra)": "community_shield_cup.png",
        "Supercoppa di Lega (Italia)": "supercoppa_italia_cup.png",
        "DFL-Supercup (Alemania)": "dfl_supercup_cup.png",
        "Trofeo de Campeones (Francia)": "trofeo_campeones_francia_cup.png",
        "Supercopa Johan Cruyff (Holanda)": "supercopa_johan_cruyff_cup.png",

        "Eredivise (Holanda)": "eredivisie_cup.png",
        "Copa Coca-Cola Zero (Chile)": "copa_coca_cola_zero_cup.png",
        "Copa Argentina de Futbol (Argentina)": "copa_argentina_cup.png",
        "Copa do Brasil Série A (Brasil)": "copa_brasil_cup.png",
        "Liga de Ascenso Caixun (Chile)": "ascenso_chile_cup.png",
        "Primera B Nacional (Argentina)": "primera_b_nacional_cup.png",
    }

    temporadas_disponibles = [
        "20/21", "21/22", "22/23", "23/24", "24/25", "25/26", "26/27", "27/28",
        "28/29", "29/30", "30/31", "31/32", "32/33", "33/34", "34/35", "35/36",
        "36/37", "37/38", "38/39", "39/40", "40/41"
    ]

    temporada_orden = {temp: i for i, temp in enumerate(temporadas_disponibles)}
    RUTA_LOGOS_EQUIPOS = "C:\\Users\\GAMING\\Desktop\\Proyectos\\trofeos python\\equipos"
    client = MongoClient("mongodb://localhost:27017/")
    db = client["trophycabinet"]
    equipos_temporada = db["equipos_temporada"]
    logos_equipos = {} 
    ventana = tk.Tk()
    ventana.title(f"Trofeos Guardados - {tipo_filtro}")
    ventana.geometry("1280x720")
    ventana.configure(bg="black")

    contenedor_canvas = tk.Frame(ventana)
    contenedor_canvas.pack(fill="both", expand=True)

    canvas = tk.Canvas(contenedor_canvas, bg="white")
    scrollbar = ttk.Scrollbar(contenedor_canvas, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="white")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tarjeta_font = ("Verdana", 11)
    tarjeta_bg = "#f7f7f7"
    tarjeta_border = {"bd": 1, "relief": "solid"}
    trofeos_filtrados = list(trofeos.find({"tipo": tipo_filtro}))

    agrupados_por_temporada = {}
    for t in trofeos_filtrados:
        temp = t.get("temporada", "Desconocida")
        agrupados_por_temporada.setdefault(temp, []).append(t)

    temporadas_ordenadas = sorted(
        agrupados_por_temporada.keys(),
        key=lambda t: temporada_orden.get(t, 999)
    )

    columnas = 4
    fila_actual = 0

    for temporada in temporadas_ordenadas:
        doc_equipo = equipos.find_one({"temporada": temporada})
        nombre_equipo = f" – {doc_equipo['equipo']}" if doc_equipo else ""

        titulo = tk.Label(scrollable_frame, text=f"📆 Temporada {temporada}{nombre_equipo}",
                  bg="white", font=("Arial", 14, "bold"), anchor="w")
        titulo.grid(row=fila_actual, column=0, columnspan=columnas, sticky="w", padx=15, pady=(20, 10))
        fila_actual += 1
        equipo_nombre = t.get("equipo", "")
        equipo_logo_path = os.path.join(RUTA_LOGOS_EQUIPOS, f"{equipo_nombre}.png")
        logo_equipo_imgtk = None
        if os.path.exists(equipo_logo_path):
            img_logo = Image.open(equipo_logo_path).resize((24, 24), Image.Resampling.LANCZOS)
            logo_equipo_imgtk = ImageTk.PhotoImage(img_logo)
            logos_equipos[(temporada, equipo_nombre)] = logo_equipo_imgtk

        trofeos_temp = sorted(
            agrupados_por_temporada[temporada],
            key=lambda x: 0 if x.get("ambito") == "internacional" else 1
        )

        col = 0
        for t in trofeos_temp:
            tarjeta = tk.Frame(
                scrollable_frame,
                bg=tarjeta_bg,
                padx=10,
                pady=10,
                width=280,
                height=260,
                **tarjeta_border
            )
            tarjeta.grid_propagate(False)

            nombre = t.get("nombre", "")
            goles = t.get("goles", 0)
            asistencias = t.get("asistencias", 0)

            # Buscar imagen en el diccionario completo
            ruta_img = None
            if nombre in MAPEO_IMAGENES:
                ruta_img = os.path.join(RUTA_IMAGENES, MAPEO_IMAGENES[nombre])

            if ruta_img and os.path.exists(ruta_img):
                try:
                    img = Image.open(ruta_img)
                    img = img.resize((240, 160), Image.Resampling.LANCZOS)
                    foto = ImageTk.PhotoImage(img)
                    label_img = tk.Label(tarjeta, image=foto, bg=tarjeta_bg)
                    label_img.image = foto  # evitar que la imagen sea recolectada
                    label_img.pack(anchor="center", pady=(0, 5))
                except Exception as e:
                    print(f"Error cargando imagen: {e}")

            tk.Label(tarjeta, text=f"🏆 {nombre}", bg=tarjeta_bg, font=("Arial", 12, "bold")).pack(anchor="w")
            

            if tipo_filtro == "Individual":
                if nombre.lower().startswith("máximo goleador"):
                    tk.Label(tarjeta, text=f"Goles: {goles}", bg=tarjeta_bg, font=tarjeta_font).pack(anchor="w")
                elif nombre.lower().startswith("máximo asistente"):
                    tk.Label(tarjeta, text=f"Asistencias: {asistencias}", bg=tarjeta_bg, font=tarjeta_font).pack(anchor="w")
                else:
                    tk.Label(tarjeta, text=f"Goles: {goles}", bg=tarjeta_bg, font=tarjeta_font).pack(anchor="w")
                    tk.Label(tarjeta, text=f"Asistencias: {asistencias}", bg=tarjeta_bg, font=tarjeta_font).pack(anchor="w")
            else:
                tk.Label(tarjeta, text=f"Goles: {goles}", bg=tarjeta_bg, font=tarjeta_font).pack(anchor="w")
                tk.Label(tarjeta, text=f"Asistencias: {asistencias}", bg=tarjeta_bg, font=tarjeta_font).pack(anchor="w")

            tarjeta.grid(row=fila_actual, column=col, padx=10, pady=10, sticky="nsew")

            col += 1
            if col == columnas:
                col = 0
                fila_actual += 1

        if col != 0:
            fila_actual += 1

        for c in range(columnas):
            scrollable_frame.grid_columnconfigure(c, weight=1)

    ventana.mainloop()




import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['trophycabinet']
trofeos = db['trophies']

def ventana_agregar_trofeo(tipo_preset):
    def actualizar_competencia():
        seleccionado = entry_nombre.get()

        if tipo_preset == "Individual" and seleccionado in ["Máximo Goleador", "Máximo Asistente", "Mejor Jugador"]:
            categoria_label.grid(row=1, column=0, sticky='e', padx=5, pady=5)
            categoria_combo.grid(row=1, column=1, padx=5, pady=5)
            competencia_label.grid(row=2, column=0, sticky='e', padx=5, pady=5)
            competencia_combo.grid(row=2, column=1, padx=5, pady=5)
        elif tipo_preset == "Colectivo":
            categoria_label.grid(row=1, column=0, sticky='e', padx=5, pady=5)
            categoria_combo.grid(row=1, column=1, padx=5, pady=5)
            competencia_label.grid(row=2, column=0, sticky='e', padx=5, pady=5)
            competencia_combo.grid(row=2, column=1, padx=5, pady=5)
            entry_nombre.set("Torneo Ganado")
        else:
            categoria_label.grid_remove()
            categoria_combo.grid_remove()
            competencia_label.grid_remove()
            competencia_combo.grid_remove()

        entry_goles.config(state="normal")
        entry_asistencias.config(state="normal")

        if tipo_preset == "Colectivo":
            entry_goles.config(state="normal")
            entry_asistencias.config(state="normal")
        elif seleccionado == "Máximo Goleador":
            entry_goles.config(state="normal")
            entry_asistencias.delete(0, tk.END)
            entry_asistencias.config(state="disabled")
        elif seleccionado == "Máximo Asistente":
            entry_asistencias.config(state="normal")
            entry_goles.delete(0, tk.END)
            entry_goles.config(state="disabled")

    def actualizar_competencias_por_categoria(*args):
        categoria = categoria_combo.get()
        competencias = categorias_individuales.get(categoria, [])
        competencia_combo['values'] = competencias
        if competencias:
            competencia_combo.set(competencias[0])

    def agregar_trofeo():
        nombre_base = entry_nombre.get().strip()
        temporada = entry_temporada.get().strip()
        goles = entry_goles.get().strip()
        asistencias = entry_asistencias.get().strip()
        tipo = tipo_preset
        ambito = "local"

        if not nombre_base or not temporada:
            messagebox.showwarning("Campos incompletos", "Por favor, rellena todos los campos obligatorios.")
            return

        if tipo_preset == "Colectivo":
            nombre = competencia_combo.get().strip()
        else:
            nombre = nombre_base

        if tipo_preset == "Individual" and nombre_base in ["Máximo Goleador", "Máximo Asistente", "Mejor Jugador"]:
            competencia = competencia_combo.get().strip()
            if competencia:
                nombre += f" {competencia}"
                if any(word in competencia.lower() for word in ["champions", "europa", "conference", "libertadores", "world", "uefa", "copa américa"]):
                    ambito = "internacional"
        elif nombre_base.lower() in ["balón de oro", "bota de oro", "jugador uefa"]:
            ambito = "internacional"

        if tipo == "Colectivo":
            if any(nombre.lower() in c.lower() for cat in categorias_colectivas.values() for c in cat if any(word in c.lower() for word in ["champions", "libertadores", "world", "intercontinental", "euro", "copa américa"])):
                ambito = "internacional"

        try:
            goles_val = int(goles) if goles else 0
            asistencias_val = int(asistencias) if asistencias else 0
        except ValueError:
            messagebox.showwarning("Datos inválidos", "Goles y Asistencias deben ser números enteros.")
            return

        trofeo = {
            "nombre": nombre,
            "temporada": temporada,
            "goles": goles_val,
            "asistencias": asistencias_val,
            "tipo": tipo,
            "ambito": ambito,
        }
        trofeos.insert_one(trofeo)
        messagebox.showinfo("Éxito", f"Trofeo '{nombre}' agregado correctamente.")
        entry_nombre.set(opciones_nombre[0])
        entry_temporada.set(temporadas_disponibles[0])
        entry_goles.delete(0, tk.END)
        entry_asistencias.delete(0, tk.END)
        categoria_combo.set(list(categorias_individuales.keys())[0])
        actualizar_competencias_por_categoria()
        actualizar_competencia()

    ventana = tk.Tk()
    ventana.title(f"Agregar Trofeo - {tipo_preset}")
    ventana.geometry("560x520")

    label_font = ("Arial", 12)
    entry_font = ("Arial", 12)

    categorias_individuales = {
        "Selecciones": ["FIFA World Cup", "UEFA Eurocopa", "CONMEBOL Copa América"],
        "Competiciones Internacionales Europeas": ["UEFA Champions League", "UEFA Europa League", "UEFA Conference League","UEFA SuperCup"],
        "Competiciones Internacionales Sudamericanas": ["CONMEBOL Libertadores", "CONMEBOL Sudamericana", "CONMEBOL Recopa","CONMEBOL Copa América"],
        "Torneos Mundiales": ["Intercontinental", "FIFA Club World Cup"],
        "Ligas Nacionales Europeas": ["LaLiga EA Sports (España)", "Premier League (Inglaterra)", "Serie A TIM (Italia)", "Bundesliga (Alemania)", "Ligue 1 Uber Eats (Francia)", "Eredivise (Holanda)"],
        "Copas Nacionales Europeas": ["Copa del Rey (España)", "FA Cup (Inglaterra)", "Carabao Cup (Inglaterra)", "Coppa Italia (Italia)", "DFB-Pokal (Alemania)", "Coupe de France (Francia), KNVB Beker (Holanda)"],
        "Supercopas Nacionales Europeas": ["Supercopa de España (España)", "Community Shield (Inglaterra)", "Supercoppa di Lega (Italia)", "DFL-Supercup (Alemania)", "Trofeo de Campeones (Francia), Supercopa Johan Cruyff (Holanda)"],
        "Ligas Nacionales Sudamericanas": ["Campeonato Nacional (Chile)", "Liga de Ascenso Caixun (Chile)", "Liga Profesional de Fútbol Apertura (Argentina)","Liga Profesional de Fútbol Clausura (Argentina)", "Primera B Nacional (Argentina)", "Campeonato Brasileiro Série A (Brasil)"],
        "Copas Nacionales Sudamericanas": ["Copa Coca-Cola Zero (Chile)", "Copa Argentina de Futbol (Argentina)", "Copa do Brasil Série A (Brasil)"]
    }

    categorias_colectivas = categorias_individuales

    opciones_individuales = [
        "Balón de oro",
        "Bota de oro",
        "Máximo Goleador",
        "Máximo Asistente",
        "Mejor Jugador",
        "Jugador UEFA"
        "Jugador CONMEBOL"
    ]
    opciones_colectivos = ["Torneo Ganado"]

    opciones_nombre = opciones_individuales if tipo_preset == "Individual" else opciones_colectivos

    temporadas_disponibles = [
        "22/23","23/24", "24/25", "25/26", "26/27", "27/28", "28/29",
        "29/30", "30/31", "31/32", "32/33", "33/34", "34/35",
        "35/36", "36/37", "37/38", "38/39", "39/40", "40/41"
    ]

    tk.Label(ventana, text="Nombre:", font=label_font).grid(row=0, column=0, sticky='e', padx=5, pady=5)
    entry_nombre = ttk.Combobox(ventana, values=opciones_nombre, font=entry_font, width=28)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)
    entry_nombre.current(0)
    entry_nombre.bind("<<ComboboxSelected>>", lambda e: actualizar_competencia())

    categoria_label = tk.Label(ventana, text="Categoría:", font=label_font)
    categoria_combo = ttk.Combobox(ventana, values=list(categorias_individuales.keys()), font=entry_font, width=28)
    categoria_combo.bind("<<ComboboxSelected>>", actualizar_competencias_por_categoria)
    categoria_combo.set(list(categorias_individuales.keys())[0])

    competencia_label = tk.Label(ventana, text="Competencia:", font=label_font)
    competencia_combo = ttk.Combobox(ventana, values=[], font=entry_font, width=28)

    tk.Label(ventana, text="Temporada:", font=label_font).grid(row=3, column=0, sticky='e', padx=5, pady=5)
    entry_temporada = ttk.Combobox(ventana, values=temporadas_disponibles, font=entry_font, width=28)
    entry_temporada.grid(row=3, column=1, padx=5, pady=5)
    entry_temporada.current(0)

    tk.Label(ventana, text="Goles:", font=label_font).grid(row=5, column=0, sticky='e', padx=5, pady=5)
    entry_goles = tk.Entry(ventana, font=entry_font, width=30)
    entry_goles.grid(row=5, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Asistencias:", font=label_font).grid(row=6, column=0, sticky='e', padx=5, pady=5)
    entry_asistencias = tk.Entry(ventana, font=entry_font, width=30)
    entry_asistencias.grid(row=6, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Tipo:", font=label_font).grid(row=7, column=0, sticky='e', padx=5, pady=5)
    entry_tipo = tk.Entry(ventana, font=entry_font, width=30)
    entry_tipo.insert(0, tipo_preset)
    entry_tipo.config(state='readonly')
    entry_tipo.grid(row=7, column=1, padx=5, pady=5)

    btn_agregar = tk.Button(ventana, text="Agregar Trofeo", font=label_font, command=agregar_trofeo)
    btn_agregar.grid(row=8, column=0, columnspan=2, pady=15)

    if tipo_preset == "Individual" or tipo_preset == "Colectivo":
        actualizar_competencias_por_categoria()
        actualizar_competencia()

    ventana.mainloop()

def ventana_ver_estadisticas():
    import tkinter as tk
    from tkinter import ttk
    from pymongo import MongoClient
    from PIL import Image, ImageTk
    import os

    ruta_imagenes = "C:\\Users\\GAMING\\Desktop\\Proyectos\\trofeos python\\equipos"

    client = MongoClient("mongodb://localhost:27017/")
    db = client["trophycabinet"]
    estadisticas = db["estadisticas"]
    equipos = db["equipos_temporada"]
    datos = list(estadisticas.find())
    agrupado = {}

    ventana = tk.Tk()
    ventana.title("📊 Estadísticas por Temporada")
    ventana.geometry("1100x600")
    ventana.configure(bg="white")

    frame_scroll = tk.Frame(ventana)
    frame_scroll.pack(fill="both", expand=True)

    canvas = tk.Canvas(frame_scroll, bg="white")
    scrollbar = ttk.Scrollbar(frame_scroll, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="white")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    datos = list(estadisticas.find())
    agrupado = {}
    for est in datos:
        temp = est.get("temporada", "Desconocida")
        agrupado.setdefault(temp, []).append(est)

    temporadas_ordenadas = sorted(
        agrupado.keys(),
        key=lambda t: t.split("/")[0] if "/" in t else t
    )

    logos = {}

    for temp in temporadas_ordenadas:
       
        equipo_doc = equipos.find_one({"temporada": temp})
        nombre_equipo = equipo_doc["equipo"] if equipo_doc else "Sin equipo"

        ruta_logo = os.path.join(ruta_imagenes, f"{nombre_equipo}.png")
        logo_imagen = None
        if os.path.exists(ruta_logo):
            img = Image.open(ruta_logo)
            img = img.resize((32, 32))
            logo_imagen = ImageTk.PhotoImage(img)
            logos[temp] = logo_imagen  

        header_frame = tk.Frame(scrollable_frame, bg="white")
        header_frame.pack(pady=(15, 5), anchor="w", padx=10)

        if logo_imagen:
            tk.Label(header_frame, image=logo_imagen, bg="white").pack(side="left", padx=(0, 8))

        tk.Label(
            header_frame,
            text=f"📅 Temporada {temp} - {nombre_equipo}",
            font=("Arial", 14, "bold"),
            bg="white"
        ).pack(side="left")

        columnas = ("competencia", "partidos", "goles", "asistencias", "g_a", "g_por_partido", "amarillas", "rojas")
        tabla = ttk.Treeview(
            scrollable_frame,
            columns=columnas,
            show="headings",
            height=6
        )
        tabla.pack(padx=15, pady=5, fill="x")

        headers = {
            "competencia": "Competencia",
            "partidos": "Partidos",
            "goles": "Goles",
            "asistencias": "Asistencias",
            "g_a": "G/A",
            "g_por_partido": "G/P",
            "amarillas": "Amarillas",
            "rojas": "Rojas"
        }

        for col in columnas:
            tabla.heading(col, text=headers[col])
            tabla.column(col, anchor="center", width=110)

        total_partidos = total_goles = total_asistencias = total_amarillas = total_rojas = 0

        for est in agrupado[temp]:
            partidos = est.get("partidos", 0)
            goles = est.get("goles", 0)
            asistencias = est.get("asistencias", 0)
            amarillas = est.get("amarillas", 0)
            rojas = est.get("rojas", 0)

            g_a = goles + asistencias
            g_por_partido = round(goles / partidos, 2) if partidos > 0 else 0.0

            total_partidos += partidos
            total_goles += goles
            total_asistencias += asistencias
            total_amarillas += amarillas
            total_rojas += rojas

            tabla.insert("", "end", values=(
                est.get("competencia", ""),
                partidos,
                goles,
                asistencias,
                g_a,
                g_por_partido,
                amarillas,
                rojas
            ))

        total_g_a = total_goles + total_asistencias
        total_gpp = round(total_goles / total_partidos, 2) if total_partidos > 0 else 0.0

        tabla.insert("", "end", values=(
            "TOTAL",
            total_partidos,
            total_goles,
            total_asistencias,
            total_g_a,
            total_gpp,
            total_amarillas,
            total_rojas
        ))

    ventana.mainloop()


def ventana_agregar_estadisticas():
    def actualizar_competencias_por_categoria(*args):
        categoria = categoria_combo.get()
        competencias = categorias_individuales.get(categoria, [])
        competencia_combo['values'] = competencias
        if competencias:
            competencia_combo.set(competencias[0])

    def guardar_estadisticas():
        competencia = competencia_combo.get().strip()
        temporada = entry_temporada.get().strip()

        try:
            pj = int(entry_pj.get() or 0)
            goles = int(entry_goles.get() or 0)
            asist = int(entry_asist.get() or 0)
            amarillas = int(entry_amarillas.get() or 0)
            rojas = int(entry_rojas.get() or 0)
        except ValueError:
            messagebox.showwarning("Error", "Todos los valores deben ser enteros.")
            return

        if not competencia or not temporada:
            messagebox.showwarning("Error", "Debes completar competencia y temporada.")
            return

        filtro = {"competencia": competencia, "temporada": temporada}
        existente = estadisticas.find_one(filtro)

        if existente:
            nueva_data = {
                "partidos": existente["partidos"] + pj,
                "goles": existente["goles"] + goles,
                "asistencias": existente["asistencias"] + asist,
                "amarillas": existente["amarillas"] + amarillas,
                "rojas": existente["rojas"] + rojas,
            }
            estadisticas.update_one(filtro, {"$set": nueva_data})
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

        messagebox.showinfo("Guardado", "Estadísticas actualizadas correctamente.")
        for entry in [entry_pj, entry_goles, entry_asist, entry_amarillas, entry_rojas]:
            entry.delete(0, tk.END)

    ventana = tk.Tk()
    ventana.title("Agregar Estadísticas")
    ventana.geometry("450x430")

    label_font = ("Arial", 12)
    entry_font = ("Arial", 12)

    categorias_individuales = {
        "Selecciones": ["FIFA World Cup", "UEFA Eurocopa", "CONMEBOL Copa América", "CONMEBOL Clasificatorias Mundial", "UEFA Clasificatorias Mundial"],
        "Competiciones Internacionales Europeas": ["UEFA Champions League", "UEFA Europa League", "UEFA Conference League","UEFA SuperCup"],
        "Competiciones Internacionales Sudamericanas": ["CONMEBOL Libertadores", "CONMEBOL Sudamericana", "CONMEBOL Recopa","CONMEBOL Copa América"],
        "Torneos Mundiales": ["Intercontinental", "FIFA Club World Cup"],
        "Ligas Nacionales Europeas": ["LaLiga EA Sports (España)", "Premier League (Inglaterra)", "Serie A TIM (Italia)", "Bundesliga (Alemania)", "Ligue 1 Uber Eats (Francia)", "Eredivise (Holanda)"],
        "Copas Nacionales Europeas": ["Copa del Rey (España)", "FA Cup (Inglaterra)", "Carabao Cup (Inglaterra)", "Coppa Italia (Italia)", "DFB-Pokal (Alemania)", "Coupe de France (Francia), KNVB Beker (Holanda)"],
        "Supercopas Nacionales Europeas": ["Supercopa de España (España)", "Community Shield (Inglaterra)", "Supercoppa di Lega (Italia)", "DFL-Supercup (Alemania)", "Trofeo de Campeones (Francia), Supercopa Johan Cruyff (Holanda)"],
        "Ligas Nacionales Sudamericanas": ["Campeonato Nacional (Chile)", "Liga de Ascenso Caixun (Chile)", "Liga Profesional de Fútbol Apertura (Argentina)","Liga Profesional de Fútbol Clausura (Argentina)", "Primera B Nacional (Argentina)", "Campeonato Brasileiro Série A (Brasil)"],
        "Copas Nacionales Sudamericanas": ["Copa Coca-Cola Zero (Chile)", "Copa Argentina de Futbol (Argentina)", "Copa do Brasil Série A (Brasil)"]
    }

    tk.Label(ventana, text="Categoría:", font=label_font).grid(row=0, column=0, sticky='e', padx=10, pady=5)
    categoria_combo = ttk.Combobox(ventana, values=list(categorias_individuales.keys()), font=entry_font, width=28)
    categoria_combo.grid(row=0, column=1, padx=10, pady=5)
    categoria_combo.set(list(categorias_individuales.keys())[0])
    categoria_combo.bind("<<ComboboxSelected>>", actualizar_competencias_por_categoria)

    tk.Label(ventana, text="Competencia:", font=label_font).grid(row=1, column=0, sticky='e', padx=10, pady=5)
    competencia_combo = ttk.Combobox(ventana, values=[], font=entry_font, width=28)
    competencia_combo.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Temporada:", font=label_font).grid(row=2, column=0, sticky='e', padx=10, pady=5)
    entry_temporada = ttk.Combobox(ventana, values=[
        "22/23","23/24", "24/25", "25/26", "26/27", "27/28", "28/29",
        "29/30", "30/31", "31/32", "32/33", "33/34", "34/35",
        "35/36", "36/37", "37/38", "38/39", "39/40", "40/41"
    ], font=entry_font, width=28)
    entry_temporada.grid(row=2, column=1, padx=10, pady=5)
    entry_temporada.current(0)

    campos_estadisticos = [
        ("Partidos Jugados:", "entry_pj"),
        ("Goles:", "entry_goles"),
        ("Asistencias:", "entry_asist"),
        ("Tarjetas Amarillas:", "entry_amarillas"),
        ("Tarjetas Rojas:", "entry_rojas"),
    ]

    entries = {}

    for idx, (texto, clave) in enumerate(campos_estadisticos, start=3):
        tk.Label(ventana, text=texto, font=label_font).grid(row=idx, column=0, sticky='e', padx=10, pady=5)
        entry = tk.Entry(ventana, font=entry_font, width=30)
        entry.grid(row=idx, column=1, padx=10, pady=5)
        entries[clave] = entry

    entry_pj = entries["entry_pj"]
    entry_goles = entries["entry_goles"]
    entry_asist = entries["entry_asist"]
    entry_amarillas = entries["entry_amarillas"]
    entry_rojas = entries["entry_rojas"]

    tk.Button(ventana, text="Guardar Estadísticas", font=("Arial", 12), command=guardar_estadisticas)\
        .grid(row=8, column=0, columnspan=2, pady=20)

    actualizar_competencias_por_categoria()
    ventana.mainloop()


def agregar_equipo_temporada():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["trophycabinet"]
    equipos = db["equipos_temporada"]

    temporadas_disponibles = [
        "22/23","23/24", "24/25", "25/26", "26/27", "27/28", "28/29",
        "29/30", "30/31", "31/32", "32/33", "33/34", "34/35",
        "35/36", "36/37", "37/38", "38/39", "39/40", "40/41"
    ]

    equipos_disponibles = [
        "FC Barcelona",
        "CSD Colo-Colo",
        "Deportes Temuco",
        "Boca Juniors"
    ]

    ventana = tk.Tk()
    ventana.title("Agregar/Actualizar Equipo por Temporada")
    ventana.geometry("420x220")

    tk.Label(ventana, text="Seleccionar Temporada:", font=("Arial", 12)).pack(pady=(15,5))
    combo_temporada = ttk.Combobox(ventana, values=temporadas_disponibles, font=("Arial", 12), state="readonly")
    combo_temporada.pack()
    combo_temporada.current(0)

    tk.Label(ventana, text="Seleccionar Equipo:", font=("Arial", 12)).pack(pady=(15,5))
    combo_equipo = ttk.Combobox(ventana, values=equipos_disponibles, font=("Arial", 12), state="readonly")
    combo_equipo.pack()
    combo_equipo.current(0)

    def guardar_equipo():
        temporada = combo_temporada.get()
        equipo = combo_equipo.get()

        if not temporada or not equipo:
            messagebox.showwarning("Campos incompletos", "Por favor, selecciona una temporada y un equipo.")
            return

        existente = equipos.find_one({"temporada": temporada})
        if existente:
            equipos.update_one({"temporada": temporada}, {"$set": {"equipo": equipo}})
            messagebox.showinfo("Actualizado", f"Equipo actualizado para la temporada {temporada}.")
        else:
            equipos.insert_one({"temporada": temporada, "equipo": equipo})
            messagebox.showinfo("Registrado", f"Equipo '{equipo}' registrado para la temporada {temporada}.")

    btn_guardar = tk.Button(ventana, text="Guardar Equipo", font=("Arial", 12), command=guardar_equipo)
    btn_guardar.pack(pady=20)

    ventana.mainloop()

    RUTA_LOGOS = "C:\\Users\\GAMING\\Desktop\\Proyectos\\trofeos python\\equipos" 

    ventana = tk.Tk()
    ventana.title("Agregar/Actualizar Equipo por Temporada")
    ventana.geometry("450x300")

    tk.Label(ventana, text="Seleccionar Temporada:", font=("Arial", 12)).pack(pady=(15,5))
    combo_temporada = ttk.Combobox(ventana, values=temporadas_disponibles, font=("Arial", 12), state="readonly")
    combo_temporada.pack()
    combo_temporada.current(0)

    tk.Label(ventana, text="Seleccionar Equipo:", font=("Arial", 12)).pack(pady=(15,5))
    combo_equipo = ttk.Combobox(ventana, values=equipos_disponibles, font=("Arial", 12), state="readonly")
    combo_equipo.pack()
    combo_equipo.current(0)

    label_logo = tk.Label(ventana, bg="white")
    label_logo.pack(pady=10)

    def actualizar_logo(event=None):
        equipo = combo_equipo.get()
        nombre_archivo = equipo.lower().replace(" ", "_").replace(".", "") + ".png"
        ruta_img = os.path.join(RUTA_LOGOS, nombre_archivo)
        if os.path.exists(ruta_img):
            try:
                img = Image.open(ruta_img)
                img = img.resize((100, 100), Image.Resampling.LANCZOS)
                foto = ImageTk.PhotoImage(img)
                label_logo.config(image=foto)
                label_logo.image = foto  # evitar recolección basura
            except Exception as e:
                label_logo.config(image=None)
                label_logo.image = None
                print(f"Error cargando imagen: {e}")
        else:
            label_logo.config(image=None)
            label_logo.image = None

    combo_equipo.bind("<<ComboboxSelected>>", actualizar_logo)
    actualizar_logo() 

    def guardar_equipo():
        temporada = combo_temporada.get()
        equipo = combo_equipo.get().strip()

        if not equipo:
            messagebox.showwarning("Campos incompletos", "Por favor, selecciona el equipo.")
            return

        existente = equipos.find_one({"temporada": temporada})
        if existente:
            equipos.update_one({"temporada": temporada}, {"$set": {"equipo": equipo}})
            messagebox.showinfo("Actualizado", f"Equipo actualizado para la temporada {temporada}.")
        else:
            equipos.insert_one({"temporada": temporada, "equipo": equipo})
            messagebox.showinfo("Registrado", f"Equipo '{equipo}' registrado para la temporada {temporada}.")

    btn_guardar = tk.Button(ventana, text="Guardar Equipo", font=("Arial", 12), command=guardar_equipo)
    btn_guardar.pack(pady=15)

    ventana.mainloop()

def menu():
    while True:
        print("\n=== Menú Vitrina de Trofeos ===")
        print("1. Ver Trofeos Individuales")
        print("2. Ver Trofeos Colectivos")
        print("3. Ver Estadisticas")
        print("4. Agregar Trofeos Individuales")
        print("5. Agregar Trofeos Colectivos")
        print("6. Editar Estadisticas")
        print("7. Agregar equipo por temporada")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            ventana_ver_trofeos("Individual")
        elif opcion == "2":
            ventana_ver_trofeos("Colectivo")
        elif opcion == "3":
            ventana_ver_estadisticas()
        elif opcion == "4":
            ventana_agregar_trofeo("Individual")
        elif opcion == "5":
            ventana_agregar_trofeo("Colectivo")
        elif opcion == "6":
            ventana_agregar_estadisticas()
        elif opcion == "7":
            agregar_equipo_temporada()
    
        elif opcion == "0":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida, intenta otra vez.")
    

if __name__ == "__main__":
    menu()
