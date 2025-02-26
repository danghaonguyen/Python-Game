import random

def game():
    number = random.randint(1, 100)
    attempts = 0

    print("🎯 Đoán số từ 1 đến 100!")

    while True:
        guess = int(input("Nhập số của bạn: "))
        attempts += 1

        if guess < number:
            print("📉 Số bạn đoán nhỏ hơn!")
        elif guess > number:
            print("📈 Số bạn đoán lớn hơn!")
        else:
            print(f"🎉 Chính xác! Bạn đã đoán đúng sau {attempts} lần.")
            break
game()