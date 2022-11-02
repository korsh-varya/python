import additional
import random

print(additional.logo)

is_game = True
score = 0
data = additional.data
a = random.choice(data)
b = random.choice(data)

while is_game:
    a = random.choice(data)
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    print("Твой счет", score)
    print("-"*10)
    print(f"A:{a['name']}. {a['description']} из {a['country']}")
    print(additional.vs)
    print(f"B:{b['name']}. {b['description']} из {b['country']}")
    select = input("У кого больше подпищиков?(А,В,МЕНЯЙ)").upper().strip()

    if select == "A" or select == "B":
        if a['follower_count'] > b['follower_count'] and select == "A":
            score = score + 1
            print("ok")
        elif a['follower_count'] < b['follower_count'] and select == "B":
            score = score + 1
            print("ok")
        else:
            print("Ты ошибся")
            is_game = False
    else:
        print("Я обиделся")
        quit()