import streamlit as st
import time
from visualizer import visualize  # Importa la función de visualización
from game import GameFire  # Asegúrate de tener esta importación correcta
from forest_fire_rules import TreeBurnRule, BurnedTreeToTree, BurnTreeToBurned

def initialize_game(config):
    return GameFire(config["rows"], config['cols'], config['rules'], config["density"])

# Configuración inicial
config = {
    "rows": 60,
    "cols": 60,
    "generations": 120,
    "rules": [TreeBurnRule, BurnTreeToBurned],  # Asegúrate de que estas reglas estén definidas en tu módulo
    "density": 0.45,
    "sleep_time": 0.2,
    "output_type": "visualizer"
}

# Título de la app
st.title("Tree Game Simulation")

# Opciones para el usuario en la interfaz de Streamlit
config["rows"] = st.sidebar.slider("Select the number of rows:", min_value=10, max_value=100, value=config["rows"])
config["cols"] = st.sidebar.slider("Select the number of columns:", min_value=10, max_value=100, value=config["cols"])
config["generations"] = st.sidebar.slider("Select the number of generations:", min_value=1, max_value=200, value=config["generations"])
config["density"] = st.sidebar.slider("Select the initial tree density:", min_value=0.1, max_value=1.0, value=config["density"])
config["sleep_time"] = st.sidebar.slider("Select the sleep time between updates (seconds):", min_value=0.1, max_value=5.0, value=config["sleep_time"])

# Inicializar el juego
game = initialize_game(config)

# Crear contenedor para el gráfico
left, right = st.columns(2)
# placeholder = st.empty()
fig_placeholder_1 = left.empty()
fig_placeholder_2 = right.empty()

# Comenzar la simulación
if config["output_type"] == "visualizer":
    # left, right = st.columns(2)
    for fig, fig2 in visualize(game, config["generations"], config["sleep_time"]):
        with fig_placeholder_1.container():
            # left.pyplot(fig)
            # right.pyplot(fig2)
            st.pyplot(fig)
            # st.pyplot(fig2)
        with fig_placeholder_2.container():
            st.pyplot(fig2)
        time.sleep(config["sleep_time"])


# with st.sidebar:
#     rows = st.slider("Number of rows:", min_value=10, max_value=100, value=60)
#     cols = st.slider("Number of columns:", min_value=10, max_value=100, value=60)
#     generations = st.slider("Number of generations:", min_value=1, max_value=200, value=120)
#     density = st.slider("Initial tree density:", min_value=0.1, max_value=1.0, value=0.45)
#     sleep_time = st.slider("Sleep time between updates (seconds):", min_value=0.1, max_value=5.0, value=0.2)

# # Configuración inicial
# config = {
#     "rows": rows,
#     "cols": cols,
#     "generations": generations,
#     "rules": [TreeBurnRule, BurnTreeToBurned],  # Asegúrate de que estas reglas estén definidas en tu módulo
#     "density": density,
#     "sleep_time": sleep_time,
#     "output_type": "visualizer"
# }

# # Inicializar el juego
# game = initialize_game(config)

# # Crear columnas para los gráficos
# left, right = st.columns(2)
# fig_placeholder1 = left.empty()
# fig_placeholder2 = right.empty()

# # Comenzar la simulación
# if config["output_type"] == "visualizer":
#     for fig, fig2 in visualize(game, config["generations"], config["sleep_time"]):
#         # Actualizar los gráficos en los placeholders
#         with fig_placeholder1.container():
#             left.pyplot(fig)
#         with fig_placeholder2.container():
#             right.pyplot(fig2)

#         # Pausar para la siguiente iteración
#         time.sleep(config["sleep_time"])

# import streamlit as st
# import time
# import matplotlib.pyplot as plt
# import numpy as np
# from visualizer import visualize  # Asegúrate de que esta función esté correctamente importada
# from game import GameFire  # Asegúrate de tener esta importación correcta
# from forest_fire_rules import TreeBurnRule, BurnedTreeToTree, BurnTreeToBurned

# def initialize_game(config):
#     return GameFire(config["rows"], config['cols'], config['rules'], config["density"])

# # Título de la app
# st.title("Tree Game Simulation")

# # Configuración en el sidebar
# with st.sidebar:
#     rows = st.slider("Number of rows:", min_value=10, max_value=100, value=60)
#     cols = st.slider("Number of columns:", min_value=10, max_value=100, value=60)
#     generations = st.slider("Number of generations:", min_value=1, max_value=200, value=120)
#     density = st.slider("Initial tree density:", min_value=0.1, max_value=1.0, value=0.45)
#     sleep_time = st.slider("Sleep time between updates (seconds):", min_value=0.1, max_value=5.0, value=0.2)

# # Configuración inicial
# config = {
#     "rows": rows,
#     "cols": cols,
#     "generations": generations,
#     "rules": [TreeBurnRule, BurnTreeToBurned],  # Asegúrate de que estas reglas estén definidas en tu módulo
#     "density": density,
#     "sleep_time": sleep_time,
#     "output_type": "visualizer"
# }

# # Inicializar el juego
# game = initialize_game(config)

# # Crear columnas para los gráficos
# left, right = st.columns(2)
# fig_placeholder1 = left.empty()
# fig_placeholder2 = right.empty()

# # Comenzar la simulación
# if config["output_type"] == "visualizer":
#     # Crear las figuras fuera del bucle para evitar recrearlas en cada iteración
#     fig, ax = plt.subplots()
#     fig2, ax2 = plt.subplots()

#     # Iterar a través de las generaciones
#     for frame in visualize(game, config["generations"], config["sleep_time"]):
#         # Actualizar el gráfico principal
#         ax.clear()
#         ax.imshow(game.grid.grid, cmap=frame[0].get_cmap(), norm=frame[0].norm)
#         ax.set_xticks([])
#         ax.set_yticks([])

#         # Actualizar el gráfico de barras
#         ax2.clear()
#         ax2.plot(np.arange(len(game.tree_alives)), game.tree_alives, label='Healthy Trees', color='green')
#         ax2.plot(np.arange(len(game.tree_burned)), game.tree_burned, label='Burned Trees', color='black')
#         ax2.set_xlabel('Generation')
#         ax2.set_ylabel('Count')
#         ax2.legend()

#         # Mostrar los gráficos actualizados
#         with fig_placeholder1.container():
#             left.pyplot(fig)
#         with fig_placeholder2.container():
#             right.pyplot(fig2)

#         # Pausar para la siguiente iteración
#         time.sleep(config["sleep_time"])
