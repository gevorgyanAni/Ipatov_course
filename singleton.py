# Класс `Database` должен гарантировать наличие единственного экземпляра и предоставлять метод `connect`, который возвращает строку "Connected to the database".
#
# - Класс `Database` должен быть реализован с использованием паттерна Singleton.
# - Должен быть метод `connect`, который имитирует подключение к базе данных и возвращает строку "Connected to the database".
# - Написать тесты для проверки корректности работы Singleton (проверить, что оба экземпляра класса `Database` являются одним и тем же объектом).


class Database:
    _instance = None

    def __new__(cls): #cls – это ссылка на текущий класс
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def connect(self):
        return "Connected to the database"


db1 = Database()
db2 = Database()
print(db1.connect())  # Вывод: Connected to the database
print(db1 is db2) #db1 и db2 указывают на один и тот же объект
