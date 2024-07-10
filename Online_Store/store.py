import json
from datetime import datetime


# ТЗ: просмотр, добавление, оформление, сохранение, orders.json
# классы: Product, DiscountedProduct(наследование от Product!), для представления товаров со скидкой
# Cart - управление корзиной, Order - представление заказа,
# OnlineStore - управление магазином


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
        return f"{self.name} - {self.description} - {self.get_price} руб. (Скидка: {self.discount}%)"


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def show_cart(self):
        if not self.items:
            print("В корзине нет товаров.")
        else:
            for i, item in enumerate(self.items):
                print(f"{i + 1}. {item}")

    def total_price(self):
        total_price = sum(item.get_price() for item in self.items)
        return total_price


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
            "total_price": self.cart.total_price()
        }

    def __str__(self):
        return (f"Заказ клиента: {self.customer_name}\nАдрес: {self.customer_address}\n"
                f"Товары: {[str(item) for item in self.cart.items]}\nИтого: {self.cart.total_price()} руб.")


class OnlineStore:
    def __init__(self):
        products_file = 'products.json.'
        orders_file = 'orders.json'
        self.products_file = products_file
        self.orders_file = orders_file
        self.cart = Cart()
        self.products = self.load_products()
        self.orders = self.load_orders()
        self.orders = []
        self.products = []

    def save_products(self):  # сохраняет задачу!!использовать каждый раз
        try:
            with open(self.products_file, 'w', encoding='utf-8') as file:
                json.dump([product.to_dict() for product in self.products], file, ensure_ascii=False,
                          indent=4)  # сохраняет задачи в файл в формате JSON, отступы в 4 пробела
        except Exception as e:
            print(f"Ошибка при выгрузке товаров: {e}")

    def save_orders(self):
        try:
            with open(self.orders_file, 'w', encoding='utf-8') as file:
                json.dump([order.to_dict() for order in self.orders], file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении заказов: {e}")

    def load_orders(self):
        try:
            with open(self.orders_file, 'r', encoding='utf-8') as file:
                orders_data = json.load(file)
                for order in orders_data:
                    cart = Cart()
                    for item in orders_data['items']:
                        if 'discount' in item:
                            cart.add_product(DiscountedProduct(**item))
                        else:
                            cart.add_product(Product(**item))
                    order = Order(orders_data['customer_name'], orders_data['customer_address'], cart)
                    self.orders.append(order)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Ошибка при загрузке товаров: {e}")

    def load_products(self):  # работа с файлом, загружает товары из файла
        try:
            with open(self.products_file, 'r', encoding='utf-8') as file:
                products_data = json.load(file)
                for item in products_data:
                    if 'discount' in item:
                        self.products.append(DiscountedProduct(**item))
                    else:
                        self.products.append(Product(**item))
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
            store.print_products()
            try:
                index = int(input("Выберите товар, который хотите добавить в корзину (1-3): ")) - 1
                if 0 <= index < len(store.products):
                    store.cart.add_product(store.products[index])
                else:
                    print("Некорректный индекс товара.")
            except ValueError:
                print("Пожалуйста, введите корректный номер товара.")

        elif choice == '3':
            print('Товары в корзине: ')
            store.cart.show_cart()
        elif choice == '3':
            print('Оформление заказа: ')
            user_name = input('Напишите ваше имя: ')
            user_adress = input('Напишите адрес для доставки: ')


        elif choice == '5':
            if not store.orders:
                print("История заказов пуста.")
            else:
                for order in store.orders:
                    print(order)
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 6.")


if __name__ == "__main__":
    main()
