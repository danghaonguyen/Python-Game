#Snake game version 1

import pygame
import time
import random

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình game
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 10

# Màu sắc
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
BLACK = (0, 0, 0)

# Khởi tạo cửa sổ game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game by Haonguyen 🐍")

# Định dạng font chữ
font = pygame.font.SysFont("bahnschrift", 25)

# Hàm hiển thị điểm số
def show_score(score):
    value = font.render(f"Score: {score}", True, WHITE)
    screen.blit(value, [10, 10])

# Hàm chính của game
def game_loop():
    game_over = False
    game_close = False

    # Khởi tạo vị trí ban đầu của rắn
    x, y = WIDTH // 2, HEIGHT // 2
    x_change, y_change = 0, 0

    snake_body = []
    snake_length = 1

    # Tạo thức ăn ngẫu nhiên
    food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    clock = pygame.time.Clock()
    speed = 15  # Tốc độ di chuyển

    while not game_over:
        while game_close:
            screen.fill(BLACK)
            game_over_text = font.render("Game Over! Press R to Restart", True, RED)
            screen.blit(game_over_text, [WIDTH // 6, HEIGHT // 3])
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_loop()  # Chơi lại
                    elif event.key == pygame.K_q:
                        game_over = True
                        game_close = False

        # Xử lý sự kiện bàn phím
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change, y_change = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change, y_change = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and y_change == 0:
                    x_change, y_change = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and y_change == 0:
                    x_change, y_change = 0, BLOCK_SIZE

        # Cập nhật vị trí rắn
        x += x_change
        y += y_change

        # Kiểm tra nếu rắn chạm biên
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        # Vẽ màn hình game
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Cập nhật thân rắn
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_body.append(snake_head)

        if len(snake_body) > snake_length:
            del snake_body[0]

        # Kiểm tra nếu rắn tự cắn chính nó
        for block in snake_body[:-1]:
            if block == snake_head:
                game_close = True

        # Vẽ rắn
        for block in snake_body:
            pygame.draw.rect(screen, BLUE, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

        # Hiển thị điểm số
        show_score(snake_length - 1)

        # Cập nhật màn hình
        pygame.display.update()

        # Kiểm tra nếu rắn ăn thức ăn
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            snake_length += 1
            speed += 0.5  # Tăng tốc độ khi ăn

        clock.tick(speed)  # Điều chỉnh tốc độ rắn

    pygame.quit()
    quit()

# Chạy game
game_loop()
