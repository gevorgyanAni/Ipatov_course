import json
from datetime import datetime


class Book:
    def __init__(self, title, author, description, available):
        self.title = title
        self.author = author
        self.description = description
        self.available = available

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "available": self.available
        }

    def __str__(self):
        status = 'доступно' if self.available else 'недоступно'
        return f"Книга: {self.title}. Автор: {self.author}. Описание: {self.description}. \nИнформация о наличии: {status}\n"


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(
                {
                    "title": book.title,
                    "borrow_date": book.borrow_date
                 }
            )
            return True
        return False

    def return_book(self, book):
        book.return_book()
        for borrowed in self.borrowed_books:
            if borrowed["title"] == book.title:
                borrowed["return_date"] = book.return_date

    def borrowed_books_history(self):
        return self.borrowed_books


class BorrowableBook(Book):
    def __init__(self, title, author, description, available):
        super().__init__(title, author, description, available)
        self.borrow_date = None
        self.return_date = None

    def borrow(self):
        if self.available:
            self.available = False
            self.borrow_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return True
        return False

    def return_book(self):
        if not self.available:
            self.available = True
            self.return_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return True
        return False


class Library:
    def __init__(self, books_file='books.json', users_file='users.json'):
        self.books_file = books_file
        self.users_file = users_file
        self.books = []
        self.users = []
        self.load_books()
        self.load_users()

    def load_books(self):
        try:
            with open(self.books_file, 'r', encoding='utf-8') as file:
                books_data = json.load(file)
                for item in books_data:
                    self.books.append(BorrowableBook(**item))
        except FileNotFoundError:
            print(f"Файл {self.books_file} не найден. Будет создан новый файл при сохранении книг.")
        except json.JSONDecodeError:
            print(f"Ошибка при декодировании JSON из файла {self.books_file}. Проверьте формат файла.")
        except Exception as e:
            print(f"Произошла ошибка при загрузке книг: {e}")

    def load_users(self):
        try:
            with open(self.users_file, 'r', encoding='utf-8') as file:
                users_data = json.load(file)
                for user_data in users_data:
                    user = User(user_data["name"])
                    user.borrowed_books = user_data["borrowed_books"]
                    self.users.append(user)
        except FileNotFoundError:
            print(f"Файл {self.users_file} не найден. Будет создан новый файл при сохранении пользователей.")
        except json.JSONDecodeError:
            print(f"Ошибка при декодировании JSON из файла {self.users_file}. Проверьте формат файла.")
        except Exception as e:
            print(f"Произошла ошибка при загрузке пользователей: {e}")

    def save(self, file_path, data):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Произошла ошибка при сохранении данных в файл {file_path}: {e}")

    def save_books(self):
        books_data = [book.to_dict() for book in self.books]
        self.save(self.books_file, books_data)

    def save_users(self):
        users_data = [
        {
            "name": user.name,
            "borrowed_books": user.borrowed_books
        } for user in self.users]
        self.save(self.users_file, users_data)




    def add_user(self, name):
        user = User(name)
        self.users.append(user)
        self.save_users()
        return user

    def find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def print_books(self):
        if not self.books:
            print("Нет доступных книг")
        else:
            for i, item in enumerate(self.books):
                print(f"{i + 1}. {item}")

    def borrow_book(self, user_name, book_title):
        user = self.find_user(user_name)
        if user is None:
            user = self.add_user(user_name)


        for book in self.books:
            if book.title.lower() == book_title.lower() and book.available:
                if user.borrow_book(book):
                    self.save_books()
                    self.save_users()
                    print(f"Книга '{book_title}' заимствована пользователем '{user_name}'.")
                    return
        print(f"Книга '{book_title}' недоступна.")

    def return_book(self, user_name, book_title):
        user = self.find_user(user_name)
        if user is None:
            print(f"Пользователь '{user_name}' не найден.")
            return
        for book in self.books:
            if book.title.lower() == book_title.lower() and not book.available:
                user.return_book(book)
                self.save_books()
                self.save_users()
                print(f"Книга '{book_title}' возвращена пользователем '{user_name}'.")
                return
        print(f"Книга '{book_title}' не была заимствована пользователем '{user_name}'.")

    def user_borrow_history(self, user_name):
        user = self.find_user(user_name)
        if user is None:
            print(f"Пользователь '{user_name}' не найден.")
            return
        print(f"История заимствований для '{user_name}':")
        for borrowed in user.borrowed_books_history():
            borrow_date = borrowed["borrow_date"]
            return_date = borrowed.get("return_date", "еще не возвращена")
            print(f"- {borrowed['title']}, заимствована {borrow_date}, возвращена {return_date}")


def main():
    library = Library()

    while True:
        print("\nМосковская школьная библиотека:")
        print("1. Посмотреть список доступных книг")
        print("2. Взять книгу на время")
        print("3. Вернуть книгу")
        print("4. Посмотреть историю взятых книг")
        print("5. Выйти")

        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            library.print_books()

        elif choice == '2':
            user_name = input("Введите ваше имя: ")
            book_title = input("Введите название книги: ").lower()
            library.borrow_book(user_name, book_title)

        elif choice == '3':
            user_name = input("Введите ваше имя: ")
            book_title = input("Введите название книги: ").lower()
            library.return_book(user_name, book_title)

        elif choice == '4':
            user_name = input("Введите ваше имя: ")
            library.user_borrow_history(user_name)

        elif choice == '5':
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 6.")


if __name__ == "__main__":
    main()
