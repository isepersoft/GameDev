# splash_screen.py
import pygame

class SplashScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("prog001/assets/splash_screen.jpg")  # Измените путь по необходимости
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()
            self.clock.tick(1)  # Показываем заставку 2 секунды
            running = False