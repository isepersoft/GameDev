import random
import pygame

class Game2048:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        # Генерация нового числа (2 или 4) в случайной пустой клетке
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = random.choice([2, 4])

    def draw(self, screen):
        cell_size = 100
        font = pygame.font.Font(None, 36)

        for i in range(4):
            for j in range(4):
                pygame.draw.rect(screen, (255, 255, 255), (j * cell_size, i * cell_size, cell_size, cell_size), 2)

                if self.board[i][j] != 0:
                    text_render = font.render(str(self.board[i][j]), True, (255, 255, 255))
                    text_rect = text_render.get_rect(center=(j * cell_size + cell_size // 2, i * cell_size + cell_size // 2))
                    screen.blit(text_render, text_rect)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.move("up")
                elif event.key == pygame.K_DOWN:
                    self.move("down")
                elif event.key == pygame.K_LEFT:
                    self.move("left")
                elif event.key == pygame.K_RIGHT:
                    self.move("right")

    def move(self, direction):
        # Перемещение чисел в указанном направлении
        # direction: "up", "down", "left", "right"
        if direction == "up":
            self.move_up()
        elif direction == "down":
            self.move_down()
        elif direction == "left":
            self.move_left()
        elif direction == "right":
            self.move_right()

    def merge_tiles(self, values):
        # Сложение чисел в ряду
        for i in range(len(values) - 1):
            if values[i] == values[i + 1]:
                values[i] *= 2
                self.score += values[i]
                values.pop(i + 1)
                values.append(0)
        return values

    def move_up(self):
        for j in range(4):
            # Сжимаем все числа вверх
            values = [self.board[i][j] for i in range(4) if self.board[i][j] != 0]
            merged = self.merge_tiles(values)
            merged += [0] * (4 - len(merged))
            # Записываем результат обратно в столбец
            for i in range(4):
                self.board[i][j] = merged[i]
        self.add_new_tile()

    def move_down(self):
        for j in range(4):
            values = [self.board[i][j] for i in range(3, -1, -1) if self.board[i][j] != 0]
            merged = self.merge_tiles(values)
            merged = [0] * (4 - len(merged)) + merged
            for i in range(4):
                self.board[i][j] = merged[3 - i]
        self.add_new_tile()

    def move_left(self):
        for i in range(4):
            values = [val for val in self.board[i] if val != 0]
            merged = self.merge_tiles(values)
            merged += [0] * (4 - len(merged))
            self.board[i] = merged
        self.add_new_tile()

    def move_right(self):
        for i in range(4):
            values = [val for val in self.board[i] if val != 0]
            merged = self.merge_tiles(values)
            merged = [0] * (4 - len(merged)) + merged
            self.board[i] = merged[::-1]
        self.add_new_tile()

    def is_win(self):
        # Проверка победы (наличие числа 2048 на поле)
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 2048:
                    return True
        return False

    def is_game_over(self):
        # Проверка поражения (отсутствие доступных ходов)
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    return False  # Есть пустые клетки, игра не окончена
                if i < 3 and self.board[i][j] == self.board[i + 1][j]:
                    return False  # Есть возможность объединения в вертикальном направлении
                if j < 3 and self.board[i][j] == self.board[i][j + 1]:
                    return False  # Есть возможность объединения в горизонтальном направлении
        return True  # Нет доступных ходов, игра окончена