import random
while True:
    print("Угадай число")
    try:
        difficult = int(input("Введи максимальное число для угадования"))
        if difficult < 1:
            raise Exception
    except Exception:
        print("Число > 0 ")
        continue
    mini = 0
    maxi = difficult
    computer_number = random.randint(0, difficult)
    life = 7
    while life > 0:
        try:
            user_number = int(input("Введи число: "))
        except ValueError:
            print("Надо цифру")
            continue
        if user_number < 0 or user_number > 100:
            print(f"Введи число от 0 до {difficult}")
            continue
        if computer_number == user_number:
            print("Вы победили!")
            break
        elif computer_number < user_number:
            print("Нужно меньше.")
            maxi = user_number
        else:
            print("Нужно больше.")
            mini = user_number
        print(f">>> Интервал: {mini} – {maxi}")
        life = life - 1
        print("❤️:", life)
    answer = input("Хочешь продолжить?")
    if answer == "да":
        continue
    else:
        break
