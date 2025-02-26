import curses
import random

# Hàm main của game
def game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    w, h = sw // 2, sh // 2

    snake = [[h, w], [h, w - 1], [h, w - 2]]
    food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
    stdscr.addch(food[0], food[1], "*")

    key = curses.KEY_RIGHT
    direction = key

    while True:
        next_key = stdscr.getch()
        key = key if next_key == -1 else next_key

        if key in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN]:
            direction = key

        new_head = [snake[0][0], snake[0][1]]

        if direction == curses.KEY_DOWN:
            new_head[0] += 1
        elif direction == curses.KEY_UP:
            new_head[0] -= 1
        elif direction == curses.KEY_LEFT:
            new_head[1] -= 1
        elif direction == curses.KEY_RIGHT:
            new_head[1] += 1

        # Kiểm tra va chạm
        if new_head in snake or new_head[0] in [0, sh] or new_head[1] in [0, sw]:
            stdscr.addstr(sh // 2, sw // 4, "GAME OVER!", curses.A_BOLD)
            stdscr.refresh()
            curses.napms(2000)
            break

        snake.insert(0, new_head)

        # Kiểm tra ăn mồi
        if new_head == food:
            food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
            stdscr.addch(food[0], food[1], "*")
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], " ")

        stdscr.addch(new_head[0], new_head[1], "#")

# Khởi động game
curses.wrapper(game)
