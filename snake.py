import matplotlib.pyplot as plt
import numpy as np
import imageio

def draw_snake(days, length):
    # Setup
    grid_size = 7  # Dias da semana
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(grid_size))
    ax.set_yticks(np.arange(grid_size))
    ax.grid(True)
    snake_body = []

    # Cria uma imagem para cada movimento da cobrinha
    images = []
    for day in days:
        snake_body.append(day)
        if len(snake_body) > length:
            snake_body.pop(0)

        # Desenha a cobrinha
        ax.clear()
        ax.grid(True)
        for body_part in snake_body:
            ax.plot(body_part[1], body_part[0], 'go', markersize=10)  # Desenha o corpo da cobrinha
        ax.plot(day[1], day[0], 'ro', markersize=10)  # Desenha a cabeça da cobrinha
        fig.canvas.draw()

        # Salva a imagem
        image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        images.append(image)

    # Gera a animação
    imageio.mimsave('snake.gif', images, fps=2)

# Gerar dias fictícios para a cobrinha percorrer (mover a cabeça)
days = [(i // 7, i % 7) for i in range(49)]
length = 5  # Tamanho da cobrinha

draw_snake(days, length)
