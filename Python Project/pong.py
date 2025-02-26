import pygame

pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🏓 Pong Horizontal")

# Màu sắc
WHITE = (255, 255, 255)

# Tọa độ vợt (chuyển sang ngang)
paddle_width = 100
paddle_height = 10
paddle1 = pygame.Rect(WIDTH//2 - paddle_width//2, 20, paddle_width, paddle_height)  # Trên
paddle2 = pygame.Rect(WIDTH//2 - paddle_width//2, HEIGHT - 30, paddle_width, paddle_height)  # Dưới

# Quả bóng
ball = pygame.Rect(WIDTH//2 - 10, HEIGHT//2 - 10, 20, 20)
ball_speed_x = 4
ball_speed_y = 4

# Vận tốc vợt
paddle_speed = 6

running = True
while running:
    pygame.time.delay(30)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Điều khiển vợt (ngang)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and paddle1.x > 0:
        paddle1.x -= paddle_speed
    if keys[pygame.K_d] and paddle1.x < WIDTH - paddle_width:
        paddle1.x += paddle_speed
    if keys[pygame.K_LEFT] and paddle2.x > 0:
        paddle2.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle2.x < WIDTH - paddle_width:
        paddle2.x += paddle_speed

    # Cập nhật vị trí bóng
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Va chạm tường trái/phải
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1

    # Va chạm vợt
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_y *= -1

    # Va chạm trên/dưới (điểm thắng)
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2  # Reset vị trí

    # Vẽ vợt và bóng
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.display.update()

pygame.quit()
