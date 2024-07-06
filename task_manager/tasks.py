import json
from datetime import datetime


class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.creation_date = datetime.now().strftime("%Y-%m-%d")
        self.due_date = due_date
        self.status = "невыполнено"

    def completed_tasks(self):
        self.status = "выполнено"

    def edit_task(self, new_description, new_due_date):
        self.description = new_description
        self.due_date = new_due_date

    def __repr__(self):
        return f"Task(description={self.description}, creation_date={self.creation_date}, due_date={self.due_date}, status={self.status})" #строковое представление объекта


class TaskManager:
    def __init__(self):
        self.filename = 'tasks.json'
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def completed_tasks(self, index):  #отметка выполнено или не выполнено
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed_tasks()
            self.save_tasks()

    def delete_task(self, index):  #удаляем задачу
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def edit_task(self, index, new_description, new_due_date):  #редактируем задачу
        if 0 <= index < len(self.tasks):
            self.tasks[index].edit_task(new_description, new_due_date)
            self.save_tasks()

    def save_tasks(self):  #сохраняет задачу!!использовать каждый раз
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump([task.__dict__ for task in self.tasks], file, ensure_ascii=False,
                          indent=4)  #сохраняет задачи в файл в формате JSON, отступы в 4 пробела
        except Exception as e:
            print(f"Ошибка при сохранении задач: {e}")

    def load_tasks(self):  #работа с файлом, загружает задачи из файла
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**task_data) for task_data in tasks_data]
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Ошибка при загрузке задач: {e}")


def print_tasks(tasks):
    if not tasks:
        print("Задач нет.")
    else:
        for i, task in enumerate(tasks):
            print(
                f"{i+1}. {task.description}, срок выполнения: {task.due_date}, статус: {task.status}, дата создания: {task.creation_date}")


def main():
    manager = TaskManager()

    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Удалить задачу")
        print("4. Показать все задачи")
        print("5. Изменить задачу")
        print("6. Выйти")

        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            description = input("Введите описание задачи: ")
            due_date = input("Введите срок выполнения задачи (в формате ГГГГ-ММ-ДД): ")
            task = Task(description, due_date) #создает новый эксемпляр\объект класса
            manager.add_task(task)

        elif choice == '2':
            print_tasks(manager.tasks)
            index = int(input("Введите номер задачи, которую хотите отметить как выполненную: ")) - 1
            manager.completed_tasks(index)
        elif choice == '3':
            print_tasks(manager.tasks)
            index = int(input("Введите номер задачи, которую хотите удалить: ")) - 1
            manager.delete_task(index)
        elif choice == '4':
            print_tasks(manager.tasks)
        elif choice == '5':
            print_tasks(manager.tasks)
            index = int(input("Введите номер задачи, которую хотите изменить: ")) - 1
            new_description = input("Введите новое описание задачи: ")
            new_due_date = input("Введите новый срок выполнения задачи (в формате ГГГГ-ММ-ДД): ")
            manager.edit_task(index, new_description, new_due_date)
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 6.")


if __name__ == "__main__":
    main()
