# menu_screen.py
import pygame

class MenuScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("prog001/assets/menu_background.jpg")  # Измените путь по необходимости
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()
            self.clock.tick(60)  # Ограничение FPS