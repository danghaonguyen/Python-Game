import curses
import random

# Hàm chính của game
def game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    plane_x = sw // 2  # Vị trí máy bay người chơi
    bullets = []  # Danh sách đạn
    enemies = []  # Danh sách kẻ địch
    score = 0

    while True:
        stdscr.clear()
        stdscr.border(0)

        # Hiển thị điểm số
        stdscr.addstr(0, 2, f" Score: {score} ", curses.A_BOLD)

        # Hiển thị máy bay người chơi
        stdscr.addch(sh - 2, plane_x, "A")

        # Sinh máy bay địch ngẫu nhiên
        if random.randint(1, 10) == 1:
            enemy_x = random.randint(1, sw - 2)
            enemies.append([1, enemy_x])

        # Cập nhật đạn
        new_bullets = []
        for y, x in bullets:
            if y > 1:
                new_bullets.append([y - 1, x])
                stdscr.addch(y - 1, x, "|")
        bullets = new_bullets

        # Cập nhật máy bay địch
        new_enemies = []
        for y, x in enemies:
            if y < sh - 2:
                new_enemies.append([y + 1, x])
                stdscr.addch(y + 1, x, "V")
        enemies = new_enemies

        # Kiểm tra va chạm
        for bullet in bullets:
            for enemy in enemies:
                if bullet[0] == enemy[0] and bullet[1] == enemy[1]:
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1

        # Kiểm tra phím bấm
        key = stdscr.getch()
        if key == ord("a") and plane_x > 1:
            plane_x -= 1
        elif key == ord("d") and plane_x < sw - 2:
            plane_x += 1
        elif key == ord(" "):  # Bắn đạn
            bullets.append([sh - 3, plane_x])
        elif key == ord("q"):  # Thoát game
            break

# Khởi động game
curses.wrapper(game)
