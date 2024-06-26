def quiz_game():
    questions_and_answers = [
        ("Как называется столица Франции?", 'Париж'),
        ("Какой самый большой океан на Земле?", 'Тихий океан'),
        ("Квадратный корень из 16?", 'Четыре'),
        ("Какое значение имеет факториал числа 5?", '120')

    ]

    correct_answers = 0
    incorrect_answers = 0

    print("Добро пожаловать в викторину!")

    for i, (question, correct_answer) in enumerate(questions_and_answers, start=1):
        print(f"Вопрос {i}: {question}")
        user_answer = input("Ваш ответ: ").strip()

        if user_answer.lower() == correct_answer.lower():
            print("Правильно!")
            correct_answers += 1
        else:
            print(f"Неправильно! Правильный ответ: {correct_answer}")
            incorrect_answers += 1


    print(f"\nИтог: {correct_answers} правильных ответов, {incorrect_answers} неправильных.")


quiz_game()
