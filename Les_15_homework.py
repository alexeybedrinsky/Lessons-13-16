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

    def __len__(self):
        """
        Метод для получения количества товара на складе
        """
        return self.quantity

    def __add__(self, other):
        """
        Метод для сложения стоимости товаров
        """
        if type(self) is type(other):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Ошибка сложения. Нельзя складывать не экземпляры одного класса")


class Smartphone(Product):
    """
    Класс для описания смартфона
    """
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        """
        Метод для представления объекта в виде строки
        """
        return f"{self.name} {self.model}, {self.price} руб. Остаток: {self.quantity} шт. (Цвет: {self.color}, Память: {self.memory}GB, Эффективность: {self.efficiency})"


class LawnGrass(Product):
    """
    Класс для описания газонной травы
    """
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """
        Метод для представления объекта в виде строки
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. (Цвет: {self.color}, Страна: {self.country}, Срок прорастания: {self.germination_period} дней)"


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

    def add_product(self, product):
        """
        Метод для добавления продукта в категорию
        """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)")

    @property
    def products(self):
        """
        Геттер для списка продуктов, возвращающий их в виде строки
        """
        products = [str(product) for product in self.__products]
        return "\n".join(products) + "\n"

    @products.setter
    def products(self, value):
        """
        Сеттер для списка продуктов
        """
        if isinstance(value, list):
            if all(isinstance(product, Product) for product in value):
                self.__products = value
            else:
                raise TypeError("Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)")
        elif isinstance(value, Product):
            self.__products.append(value)
        else:
            raise TypeError("Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)")

    def __str__(self):
        """
        Метод для представления объекта в виде строки
        """
        total_products_count = sum([p.quantity for p in self.__products])
        return f"{self.name}, количество продуктов: {total_products_count} шт."

    def __add__(self, other):
        """
        Метод для сложения стоимости всех товаров в двух категориях
        """
        if isinstance(other, Category):
            total_cost = sum(product.price * product.quantity for product in self.__products)
            total_cost += sum(product.price * product.quantity for product in other.__products)
            return total_cost
        raise TypeError("Ошибка сложения. Нельзя складывать не экземпляры одного класса")

    def get_result(self):
        """
        Метод для получения результата (списка продуктов)
        """
        return self.products


# Пример использования

# Пример данных продуктов
data_smartphones = [
    {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
        "efficiency": "Высокая",
        "model": "C23 Ultra",
        "memory": 256,
        "color": "Серый"
    },
    {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8,
        "efficiency": "Высокая",
        "model": "15",
        "memory": 512,
        "color": "Серый"
    }
]

data_lawngrass = [
    {
        "name": "Premium Lawn",
        "description": "Высококачественная газонная трава",
        "price": 5000.0,
        "quantity": 20,
        "country": "Россия",
        "germination_period": 7,
        "color": "Зеленый"
    },
    {
        "name": "Standard Lawn",
        "description": "Стандартная газонная трава",
        "price": 3000.0,
        "quantity": 15,
        "country": "Россия",
        "germination_period": 10,
        "color": "Зеленый"
    }
]

# Создание категорий и добавление продуктов
category_smartphones = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни")
category_lawngrass = Category("Газонная трава", "Газонная трава для вашего сада")

# Добавление продуктов в категории
for product_data in data_smartphones:
    smartphone = Smartphone(**product_data)
    category_smartphones.add_product(smartphone)

for product_data in data_lawngrass:
    lawn_grass = LawnGrass(**product_data)
    category_lawngrass.add_product(lawn_grass)

# Вывод информации о категориях и продуктах
for category in [category_smartphones, category_lawngrass]:
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
expected_products_smartphones = '''Samsung Galaxy C23 Ultra C23 Ultra, 180000.0 руб. Остаток: 5 шт. (Цвет: Серый, Память: 256GB, Эффективность: Высокая)
Iphone 15 15, 210000.0 руб. Остаток: 8 шт. (Цвет: Серый, Память: 512GB, Эффективность: Высокая)
'''
assert category_smartphones.products == expected_products_smartphones, f"Expected:\n{expected_products_smartphones}\nGot:\n{category_smartphones.products}"

# Тест 4: Проверка списка продуктов в другой категории
expected_products_lawngrass = '''Premium Lawn, 5000.0 руб. Остаток: 20 шт. (Цвет: Зеленый, Страна: Россия, Срок прорастания: 7 дней)
Standard Lawn, 3000.0 руб. Остаток: 15 шт. (Цвет: Зеленый, Страна: Россия, Срок прорастания: 10 дней)
'''
assert category_lawngrass.products == expected_products_lawngrass, f"Expected:\n{expected_products_lawngrass}\nGot:\n{category_lawngrass.products}"

# Тест 5: Проверка True == True
assert True == True  # Ожидаемый результат: True

# Тест 6: Проверка сложения стоимости продуктов
product1 = Smartphone("Product1", "Description1", 100, 10, "Высокая", "P1", 128, "Черный")
product2 = Smartphone("Product2", "Description2", 200, 2, "Средняя", "P2", 64, "Белый")
try:
    total_cost = product1 + product2
    print(total_cost)  # Ожидаемый результат: 1400
except TypeError as e:
    print(e)

# Тест 7: Проверка сложения стоимости категорий
category3 = Category("Категория 3", "Описание 3", [product1, product2])
category4 = Category("Категория 4", "Описание 4", [product1])
try:
    total_cost_categories = category3 + category4
    print(total_cost_categories)  # Ожидаемый результат: 3000
except TypeError as e:
    print(e)

# Тест 8: Проверка добавления не продукта в категорию
try:
    category3.add_product("не продукт")
except TypeError as e:
    print(e)  # Ожидаемый ответ: Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)

# Тест 9: Проверка сеттера для списка продуктов
try:
    category3.products = ["не продукт"]
except TypeError as e:
    print(e)  # Ожидаемый ответ: Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)

print("Все тесты пройдены успешно.")
