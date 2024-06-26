import random


def guess_the_number():
    random_number = random.randint(1, 100)
    print("Я загадал число от 1 до 100. Попробуйте угадать!")
    while random_number < 101:
        try:
            user_number = int(input('Введите вашу догадку: '))

            if random_number > user_number:
                print('Мое число больше!')
            elif random_number < user_number:
                print('Мое число меньше!')
            else:
                print(f'Вы угадали! Мое число было {random_number}')
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")


guess_the_number()
