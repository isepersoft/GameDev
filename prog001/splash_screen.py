import pygame
import sys

class SplashScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("prog001/assets/splash_screen.jpg")
        self.delay_time = 5000  # время задержки в миллисекундах (5 секунд)
        
    def run(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
        pygame.time.delay(self.delay_time)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # Заставка
    splash = SplashScreen(screen)
    splash.run()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()