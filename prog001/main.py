import pygame
import sys

# Инициализация Pygame
pygame.init()

# Создание окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Моя Первая Игра")

# Основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Здесь добавь код для отрисовки и обработки событий

    pygame.display.flip()