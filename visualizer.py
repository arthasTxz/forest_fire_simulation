# import matplotlib.pyplot as plt
# from matplotlib import colors
# import matplotlib.patches as mpatches
# import numpy as np

# def visualize(game, generations, sleep_time):
#     colors_list = ['lightgrey', 'green', 'red', 'black']
#     cmap = colors.ListedColormap(colors_list)
#     bounds = [0, 1, 2, 3, 4]
#     norm = colors.BoundaryNorm(bounds, cmap.N)

#     fig, ax = plt.subplots()
    
#     game_display = ax.imshow(game.grid.grid, cmap=cmap, norm=norm, interpolation='none')
#     patches = [mpatches.Patch(color=colors_list[0], label="empty"), mpatches.Patch(color=colors_list[1], label="healthy") , mpatches.Patch(color=colors_list[2], label="burning"), mpatches.Patch(color=colors_list[3], label="burned")]
#     plt.legend(handles=patches, bbox_to_anchor=(1.1, 0),
#               ncol=4, fancybox=True, shadow=True)
#     ax.set_xticks([])
#     ax.set_yticks([])

#      # Crear la figura y el eje para el segundo gráfico
#     fig2, ax2 = plt.subplots()
#     ax2.set_title('Number of Trees')
#     ax2.set_xlabel('Generation')
#     ax2.set_ylabel('Count')
#     healthy_trees, burned_trees = [], []
#     line1, = ax2.plot([], [], label='Healthy Trees', color='green')
#     line2, = ax2.plot([], [], label='Burned Trees', color='black')
#     ax2.legend()

#     def update_tree_counts():
#         healthy = game.tree_alives  # Usar la función de conteo de árboles saludables
#         burned = game.tree_burned   # Usar la función de conteo de árboles quemados
#         healthy_trees.append(healthy)
#         burned_trees.append(burned)
#         line1.set_data(np.arange(len(healthy_trees)), healthy_trees)
#         line2.set_data(np.arange(len(burned_trees)), burned_trees)
#         ax2.relim()
#         ax2.autoscale_view()


#     for generation in range(generations):
#         # print(game.grid.grid)
#         if generation == 0:
#             for x in range(game.grid.rows):
#                 if game.grid.grid[x][0] == 1:
#                     game.grid.grid[x][0] = 2
#                 # for _ in range(game.grid.cols):

#         game.update()
#         game_display.set_data(game.grid.grid)
#         update_tree_counts()
#         plt.draw()
#         plt.pause(sleep_time)

#         plt.figure(fig2.number)
#         plt.draw()
#         plt.pause(sleep_time)

#     plt.show()


# import matplotlib.pyplot as plt
# import matplotlib.colors as colors
# import matplotlib.patches as mpatches
# import numpy as np

# def visualize(game, generations, sleep_time):
#     colors_list = ['lightgrey', 'green', 'red', 'black']
#     cmap = colors.ListedColormap(colors_list)
#     bounds = [0, 1, 2, 3, 4]
#     norm = colors.BoundaryNorm(bounds, cmap.N)

#     fig, ax = plt.subplots()
#     game_display = ax.imshow(game.grid.grid, cmap=cmap, norm=norm, interpolation='none')
#     patches = [mpatches.Patch(color=colors_list[0], label="empty"), 
#                mpatches.Patch(color=colors_list[1], label="healthy"),
#                mpatches.Patch(color=colors_list[2], label="burning"), 
#                mpatches.Patch(color=colors_list[3], label="burned")]
#     ax.legend(handles=patches, bbox_to_anchor=(1.1, 0), ncol=4, fancybox=True, shadow=True)
#     ax.set_xticks([])
#     ax.set_yticks([])

#     fig2, ax2 = plt.subplots()
#     ax2.set_title('Number of Trees')
#     ax2.set_xlabel('Generation')
#     ax2.set_ylabel('Count')
#     healthy_trees, burned_trees = [], []
#     line1, = ax2.plot([], [], label='Healthy Trees', color='green')
#     line2, = ax2.plot([], [], label='Burned Trees', color='black')
#     ax2.legend()

#     def update_tree_counts():
#         healthy = game.tree_alives
#         burned = game.tree_burned
#         healthy_trees.append(healthy)
#         burned_trees.append(burned)
#         line1.set_data(np.arange(len(healthy_trees)), healthy_trees)
#         line2.set_data(np.arange(len(burned_trees)), burned_trees)
#         ax2.relim()
#         ax2.autoscale_view()

#     for generation in range(generations):
#         if generation == 0:
#             for x in range(game.grid.rows):
#                 if game.grid.grid[x][0] == 1:
#                     game.grid.grid[x][0] = 2

#         game.update()
#         game_display.set_data(game.grid.grid)
#         update_tree_counts()
#         ax.legend(handles=patches, bbox_to_anchor=(1.1, 0), ncol=4, fancybox=True, shadow=True)
        
#         yield fig, fig2
#         plt.pause(sleep_time)

#     plt.close(fig)
#     plt.close(fig2)


import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as mpatches
import numpy as np

def visualize(game, generations, sleep_time):
    colors_list = ['lightgrey', 'green', 'red', 'black']
    cmap = colors.ListedColormap(colors_list)
    bounds = [0, 1, 2, 3, 4]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    # Crear las figuras y los ejes fuera del bucle
    fig, ax = plt.subplots()
    game_display = ax.imshow(game.grid.grid, cmap=cmap, norm=norm, interpolation='none')
    patches = [mpatches.Patch(color=colors_list[0], label="empty"), 
               mpatches.Patch(color=colors_list[1], label="healthy"),
               mpatches.Patch(color=colors_list[2], label="burning"), 
               mpatches.Patch(color=colors_list[3], label="burned")]
    ax.legend(handles=patches, bbox_to_anchor=(1.1, 0), ncol=4, fancybox=True, shadow=True)
    ax.set_xticks([])
    ax.set_yticks([])

    fig2, ax2 = plt.subplots()
    ax2.set_title('Number of Trees')
    ax2.set_xlabel('Generation')
    ax2.set_ylabel('Count')
    healthy_trees, burned_trees = [], []
    line1, = ax2.plot([], [], label='Healthy Trees', color='green')
    line2, = ax2.plot([], [], label='Burned Trees', color='black')
    ax2.legend()

    def update_tree_counts():
        healthy = game.tree_alives
        burned = game.tree_burned
        healthy_trees.append(healthy)
        burned_trees.append(burned)
        line1.set_data(np.arange(len(healthy_trees)), healthy_trees)
        line2.set_data(np.arange(len(burned_trees)), burned_trees)
        ax2.relim()
        ax2.autoscale_view()

    for generation in range(generations):
        if generation == 0:
            for x in range(game.grid.rows):
                if game.grid.grid[x][0] == 1:
                    game.grid.grid[x][0] = 2

        # Actualizar el estado del juego
        game.update()
        game_display.set_data(game.grid.grid)  # Actualizar la visualización del juego
        update_tree_counts()  # Actualizar los conteos de árboles

        yield fig, fig2  # Devolver las figuras para que se actualicen en Streamlit
        plt.pause(sleep_time)  # Pausar entre generaciones

    # Cerrar las figuras después de completar todas las generaciones
    plt.close(fig)
    plt.close(fig2)
