# menu_screen.py
import pygame
import sys
from Game2048 import Game2048

class MenuScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("prog001/assets/menu_background.jpg")
        self.clock = pygame.time.Clock()
        self.font_path = "prog001/fonts/JollySweater-Light.ttf"  # Замените на имя вашего файла шрифта
        self.font_size = 36
        self.font = pygame.font.Font(self.font_path, self.font_size)
        self.labels = [
            {"text": "Начать игру", "pos": (350, 200)},
            {"text": "Зал Славы", "pos": (350, 270)},
            {"text": "Об игре", "pos": (350, 320)}
        ]
        self.label_rects = []  # Области нажатия для текстовых меток

    def create_label_rects(self):
        for label in self.labels:
            text_render = self.font.render(label["text"], True, (255, 255, 255))
            rect = text_render.get_rect(center=label["pos"])
            self.label_rects.append(rect)

    def run(self):
        self.create_label_rects()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Левая кнопка мыши
                        for i, rect in enumerate(self.label_rects):
                            if rect.collidepoint(event.pos):
                                if self.labels[i]["text"] == "Начать игру":
                                    self.start_game()

            self.screen.blit(self.background, (0, 0))

            for label in self.labels:
                text_render = self.font.render(label["text"], True, (255, 255, 255))
                rect = text_render.get_rect(center=label["pos"])
                self.screen.blit(text_render, rect)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def start_game(self):
        # Запуск игры
        game = Game2048()
        # Здесь ты можешь добавить код для отображения игрового поля и логики игры
        while not game.is_game_over():
            game.process_events()

            self.screen.blit(self.background, (0, 0))
            game.draw(self.screen)
            pygame.display.flip()
            
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    menu = MenuScreen(screen)
    menu.run()