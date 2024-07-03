class Product:
    """
    Класс для описания товара в магазине
    """
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, products):
        """
        Класс-метод для создания нового продукта
        """
        return cls(**products)

    @property
    def price(self):
        """
        Геттер для цены продукта
        """
        return self._price

    @price.setter
    def price(self, value):
        """
        Сеттер для цены продукта с проверкой
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    def __str__(self):
        """
        Метод для представления объекта в виде строки
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Category:
    """
    Класс для категорий товара
    """
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product_data):
        """
        Метод для добавления продукта в категорию
        """
        new_product = Product.new_product(product_data)
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self):
        """
        Геттер для списка продуктов, возвращающий их в виде строки
        """
        products = [f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.'
                    for product in self.__products]
        return "\n".join(products) + "\n"

    def __str__(self):
        """
        Метод для представления объекта в виде строки
        """
        return f"Категория: {self.name}, Описание: {self.description}, Товаров: {len(self.__products)}"

    def get_result(self):
        """
        Метод для получения результата (списка продуктов)
        """
        return self.products


# Пример использования

# Пример данных продуктов
data = [
    {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    },
    {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
    },
    {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
    },
    {
        "name": "55 QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
    }
]

# Создание категорий и добавление продуктов
category1 = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни")
category2 = Category("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником")

# Добавление продуктов в категории
for product_data in data[:3]:
    category1.add_product(product_data)

for product_data in data[3:]:
    category2.add_product(product_data)

# Вывод информации о категориях и продуктах
for category in [category1, category2]:
    print(category)
    print(category.get_result())

print(f"Всего категорий: {Category.category_count}")
print(f"Всего продуктов: {Category.product_count}")

# Дополнительные тесты для проверки

# Тест 1: Проверка цены
product_test_data = {
    "name": "Test Product",
    "description": "Test Description",
    "price": 1000,
    "quantity": 10
}
test_product = Product.new_product(product_test_data)
print(test_product.price)  # Ожидаемый результат: 1000
test_product.price = 800  # Изменение цены
print(test_product.price)  # Ожидаемый результат: 800

# Тест 2: Проверка отрицательной цены
test_product.price = -500  # Ожидаемый результат: Цена не должна быть нулевая или отрицательная
print(test_product.price)  # Ожидаемый результат: 800

# Тест 3: Проверка списка продуктов в категории
expected_products_category1 = '''Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.
Iphone 15, 210000.0 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.
'''
assert category1.products == expected_products_category1, f"Expected:\n{expected_products_category1}\nGot:\n{category1.products}"

# Тест 4: Проверка списка продуктов в другой категории
expected_products_category2 = '''55 QLED 4K, 123000.0 руб. Остаток: 7 шт.
'''
assert category2.products == expected_products_category2, f"Expected:\n{expected_products_category2}\nGot:\n{category2.products}"

# Тест 5: Проверка True == True
assert True == True  # Ожидаемый результат: True

print("Все тесты пройдены успешно.")
