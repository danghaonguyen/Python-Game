import pygame
import random

pygame.init()

# Màn hình game
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🏎️ Car Racing")

# Load hình ảnh
car_img = pygame.image.load("car.png")
road_img = pygame.image.load("road.png")
obstacle_img = pygame.image.load("obstacle.png")

# Tọa độ xe
car_x = WIDTH // 2 - 25
car_y = HEIGHT - 120
car_x_change = 0

# Vị trí chướng ngại vật
obstacle_x = random.randint(0, WIDTH - 50)
obstacle_y = -100
obstacle_speed = 5

running = True
while running:
    screen.blit(road_img, (0, 0))  # Vẽ đường đua

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Điều khiển xe
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_x_change = -5
            if event.key == pygame.K_RIGHT:
                car_x_change = 5

        if event.type == pygame.KEYUP:
            car_x_change = 0

    car_x += car_x_change

    # Giới hạn xe không ra ngoài đường
    if car_x < 0:
        car_x = 0
    elif car_x > WIDTH - 50:
        car_x = WIDTH - 50

    # Cập nhật vị trí chướng ngại vật
    obstacle_y += obstacle_speed
    if obstacle_y > HEIGHT:
        obstacle_y = -100
        obstacle_x = random.randint(0, WIDTH - 50)

    # Hiển thị xe và chướng ngại vật
    screen.blit(car_img, (car_x, car_y))
    screen.blit(obstacle_img, (obstacle_x, obstacle_y))

    pygame.display.update()

pygame.quit()
