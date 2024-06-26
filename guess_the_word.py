import random

def guess_the_word():
    words = ['python', 'go', 'java', 'javascript', 'ruby']
    return random.choice(words)

def display_current_state(word, guessed_letters):
    display = [letter if letter in guessed_letters else '_' for letter in word]
    return ' '.join(display)

def game():
    word_to_guess = guess_the_word()
    guessed_letters = set()
    attempts = len(word_to_guess) + 3  # Дополнительные попытки

    print(f"Загадано слово: {len(word_to_guess) * '_'}")

    while attempts > 0:
        print("\nУгадано слово:", display_current_state(word_to_guess, guessed_letters))
        print(f"Осталось попыток: {attempts}")
        letter = input('Угадайте букву: ').lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue

        if letter in guessed_letters:
            print("Вы уже угадывали эту букву. Попробуйте другую.")
            continue

        guessed_letters.add(letter)

        if letter in word_to_guess:
            print("Правильно!")
            if all(letter in guessed_letters for letter in word_to_guess):
                print(f"\nПоздравляю! Вы угадали слово '{word_to_guess}'!")
                break
        else:
            print("Неправильно!")
            attempts -= 1

        if attempts == 0:
            print(f"\nВы исчерпали все попытки. Загаданное слово было '{word_to_guess}'.")

game()
