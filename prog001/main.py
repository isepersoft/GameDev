# main.py
import pygame
from Game2048 import Game2048
from splash_screen import SplashScreen
from menu_screen import MenuScreen

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # Заставка
    splash = SplashScreen(screen)
    splash.run()

    # Меню
    menu = MenuScreen(screen)
    menu.run()

    pygame.quit()

if __name__ == "__main__":
    main()