import json
from datetime import datetime


# ТЗ: просмотр, добавление, оформление, сохранение, orders.json
# классы: Product, DiscountedProduct(наследование от Product!), для представления товаров со скидкой
# Cart - управление корзиной, Order - представление заказа,
# OnlineStore - управление магазином
self.products = [
    {
        "name": "Зарядка",
        "price": 4000.0,
        "description": "Зарядка для ноутбука ThinkPad X1 Carbon (11th Gen, 14)"
    },
    {
        "name": "Ноутбук",
        "price": 146000.0,
        "description": "Ноутбук ThinkPad X1 Carbon (11th Gen, 14)",
        "discount": 40
    },
    {
        "name": "Чехол для ноутбука",
        "price": 4750.0,
        "description": "Черный водоустойчивый чехол для Ноутбука ThinkPad X1 Carbon (11th Gen, 14)"
    }
]



class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.price = price
        self.description = description

    def get_price(self):
        return self.price

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "description": self.description
        }

    def __str__(self):
        return f"{self.name} - {self.description} - {self.price} руб."



#
# [DiscountedProduct, Product, DiscountedProduct, DiscountedProduct, Product]

class DiscountedProduct(Product):
    def __init__(self, name, description, price, discount):
        super().__init__(name, description, price)
        self.discount = discount

    def get_price(self):
        return self.price * (1 - self.discount / 100)

    def to_dict(self):
        data = super().to_dict()
        data['discount'] = self.discount
        return data


    def __repr__(self):
        return f"{self.name} - {self.description} - {self.discounted_price} руб. (Скидка: {self.discount}%)"




class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def show_cart(self):
        if not self.items:
            print("Корзина пустая.")
        else:
            for i, item in enumerate(self.items):
                print(f"{i + 1}. {item}")

    def total_price(self):
        pass







class Order:
    def __init__(self, customer_name, customer_address, cart):
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.cart = cart


    def to_dict(self):
        return {
            "customer_name": self.customer_name,
            "customer_address": self.customer_address,
            "items": [item.to_dict() for item in self.cart.items],
            "total_price": self.cart.get_total_price()
        }


class OnlineStore:
    def __init__(self, products_file, orders_file):
        self.products_file = products_file
        self.orders_file = orders_file
        self.filename = 'products.json.json'
        self.products = self.load_products()
        self.orders = self.load_orders()

    def save_products(self):  # сохраняет задачу!!использовать каждый раз
        pass

    def save_orders(self):
        pass

    def load_orders(self):
        pass

    def load_products(self):  # работа с файлом, загружает товары из файла
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                products_data = json.load(file)
                self.products = [Product(**product_data) for product_data in products_data]  # распаковка словаря
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Ошибка при загрузке товаров: {e}")

    def print_products(self):
        if not self.products:
            print("Нет товаров в наличии.")
        else:
            for i, product in enumerate(self.products):
                print(
                    f"{i + 1}. Название {product.name}, описание товара: {product.description}, цена: {product.price}")
                if 'discount' in product:
                    print(f"Скидка: {product.discount}%")





def main():
    store = OnlineStore()

    while True:
        print("\nМеню:")
        print("1. Посмотреть товары в наличии")
        print("2. Добавить товар в корзину")
        print("3. Просмотреть корзину")
        print("4. Оформить заказ")
        print("5. Показать историю заказов")
        print("6. Выйти")

        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            print('Список товаров')
            store.print_products()

        elif choice == '2':
            index = int(input("Выберите товар, который хотите добавить в корзину (1-3: ")) - 1
            store.add_to_cart(index)

        elif choice == '3':
            print('Товары в корзине: ')
        elif choice == '3':
            print('Оформление заказа: ')
            user_name = input('Напишите ваше имя: ')
            user_adress= input('Напишите адрес для доставки: ')
            print('Сумма к оплате: ')

        elif choice == '5':
            print('История закказов: ')
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 6.")



if __name__ == "__main__":
    main()
