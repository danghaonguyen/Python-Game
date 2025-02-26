import random

options = ["búa", "kéo", "bao"]

def game():
    while True:
        player = input("Chọn búa, kéo, bao (hoặc 'thoát' để dừng): ").lower()
        if player == "thoát":
            break

        if player not in options:
            print("❌ Lựa chọn không hợp lệ!")
            continue

        computer = random.choice(options)
        print(f"🤖 Máy chọn: {computer}")

        if player == computer:
            print("⚖️ Hòa!")
        elif (player == "búa" and computer == "kéo") or \
             (player == "kéo" and computer == "bao") or \
             (player == "bao" and computer == "búa"):
            print("✅ Bạn thắng!")
        else:
            print("❌ Bạn thua!")

game()
