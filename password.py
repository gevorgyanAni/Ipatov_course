import random
import string


def generate_password(length, include_digits, include_symbol):
    chars = string.ascii_letters

    if include_digits:
        chars += string.digits

    if include_symbol:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def user_input():
    length = int(input("Введите длину пароля: "))

    include_digits = input("Включать цифры? (да/нет): ").lower() == 'да'

    include_symbol = input("Включать специальные символы? (да/нет): ").lower() == 'да'

    password = generate_password(length, include_digits, include_symbol)

    print("Сгенерированный пароль:", password)


user_input()
