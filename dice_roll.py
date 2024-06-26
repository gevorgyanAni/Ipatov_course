import random



def dice_roll(count):
    rolls = []
    total_sum = 0
    for _ in range(count):
        roll = random.randint(1, 6)
        rolls.append(roll)
        total_sum += roll
    return rolls, total_sum


def user_input():
    count = int(input("Сколько раз бросить кубик? "))
    result, total_sum = dice_roll(count)
    print("Результаты бросков:", ', '.join(map(str, result)))
    print(f"Сумма: {total_sum}")

user_input()