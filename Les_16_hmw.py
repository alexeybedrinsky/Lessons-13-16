from abc import ABC, abstractmethod


class InitPrintMixin:
    def __init_print__(self, *args):
        class_name = self.__class__.__name__
        params = ', '.join([f"'{arg}'" if isinstance(arg, str) else str(arg) for arg in args])
        print(f"{class_name}({params})")


class BaseProduct(ABC):
    def __init__(self, name, description, price, quantity):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        super().__init__()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    @abstractmethod
    def __str__(self):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, products):
        pass

    def __len__(self):
        return self.quantity

    def __add__(self, other):
        if type(self) is type(other):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Ошибка сложения. Нельзя складывать не экземпляры одного класса")


class Product(BaseProduct, InitPrintMixin):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.__init_print__(name, description, price, quantity)

    @classmethod
    def new_product(cls, products):
        return cls(**products)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', {self.price}, {self.quantity})"


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    @classmethod
    def new_product(cls, products):
        return cls(**products)

    def __str__(self):
        return f"{self.name} {self.model}, {self.price} руб. Остаток: {self.quantity} шт. (Цвет: {self.color}, Память: {self.memory}GB, Эффективность: {self.efficiency})"

    def __repr__(self):
        return f"Smartphone('{self.name}', '{self.description}', {self.price}, {self.quantity}, '{self.efficiency}', '{self.model}', {self.memory}, '{self.color}')"


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    @classmethod
    def new_product(cls, products):
        return cls(**products)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. (Цвет: {self.color}, Страна: {self.country}, Срок прорастания: {self.germination_period} дней)"

    def __repr__(self):
        return f"LawnGrass('{self.name}', '{self.description}', {self.price}, {self.quantity}, '{self.country}', {self.germination_period}, '{self.color}')"


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        if isinstance(product, BaseProduct):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)")

    @property
    def products(self):
        products = [str(product) for product in self.__products]
        return "\n".join(products) + "\n"

    @products.setter
    def products(self, value):
        if isinstance(value, list):
            if all(isinstance(product, BaseProduct) for product in value):
                self.__products = value
            else:
                raise TypeError(
                    "Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)")
        elif isinstance(value, BaseProduct):
            self.__products.append(value)
        else:
            raise TypeError("Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)")

    def __str__(self):
        total_products_count = sum([p.quantity for p in self.__products])
        return f"{self.name}, количество продуктов: {total_products_count} шт."

    def __add__(self, other):
        if isinstance(other, Category):
            total_cost = sum(product.price * product.quantity for product in self.__products)
            total_cost += sum(product.price * product.quantity for product in other.__products)
            return total_cost
        raise TypeError("Ошибка сложения. Нельзя складывать не экземпляры одного класса")

    def get_result(self):
        return self.products

    def middle_price(self):
        unique_products_count = len(self.__products)
        total_price = sum(product.price for product in self.__products)
        if unique_products_count == 0:
            return 0
        return total_price / unique_products_count


# Пример использования
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
    },
    {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14,
        "efficiency": "Высокая",
        "model": "Note 11",
        "memory": 1024,
        "color": "Синий"
    }
]

data_products = [
    {
        "name": "55 QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
    }
]

category_smartphones = Category("Смартфоны",
                                "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
category_products = Category("Продукты", "Различные продукты для теста")

for product_data in data_smartphones:
    smartphone = Smartphone.new_product(product_data)
    category_smartphones.add_product(smartphone)

for product_data in data_products:
    product = Product.new_product(product_data)
    category_products.add_product(product)

# Примеры использования новых функций
try:
    test_product = Product("Test", "Test", 1000, 10)
    print(test_product)
except ValueError as e:
    print(e)

category_test = Category("Тестовая категория", "Категория для тестирования")

test_product_2 = Smartphone("Test2", "Test2", 2000, 10, "Высокая", "Модель", 256, "Черный")
category_test.add_product(test_product_2)

test_product_3 = LawnGrass("Test3", "Test3", 3000, 10, "Россия", 7, "Зеленый")
category_test.add_product(test_product_3)

# Проверка среднего ценника
expected_middle_price = 140333.33333333334
actual_middle_price = category_smartphones.middle_price()

# Вывод всех продуктов для проверки
print("Вывод всех продуктов в категории 'Смартфоны':")
print(category_smartphones.get_result())
print("Вывод всех продуктов в категории 'Продукты':")
print(category_products.get_result())
print("Вывод всех продуктов в категории 'Тестовая категория':")
print(category_test.get_result())

# Вывод отладочной информации
print(f"Ожидаемый средний ценник: {expected_middle_price}")
print(f"Фактический средний ценник: {actual_middle_price}")

# Вычисление общей стоимости и количества для проверки
total_price = sum(product.price for product in category_smartphones._Category__products)
unique_products_count = len(category_smartphones._Category__products)
print(f"Общая стоимость: {total_price}")
print(f"Количество уникальных товаров: {unique_products_count}")
calculated_middle_price = total_price / unique_products_count
print(f"Вычисленный средний ценник: {calculated_middle_price}")

# Проверка среднего ценника с учетом точности
price_comparison_result = abs(actual_middle_price - expected_middle_price) < 1e-6
print(f"Средний ценник совпадает: {price_comparison_result}")

# Убедимся, что сравнение происходит корректно
print(f"Средний ценник совпадает с точностью до 1e-6: {abs(actual_middle_price - expected_middle_price) < 1e-6}")

# Проверка всех продуктов для соответствия ожидаемому выводу
expected_output = [
    "Smartphone('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5, 'Высокая', 'C23 Ultra', 256, 'Серый')",
    "Smartphone('Iphone 15', '512GB, Gray space', 210000.0, 8, 'Высокая', '15', 512, 'Серый')",
    "Smartphone('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14, 'Высокая', 'Note 11', 1024, 'Синий')",
    "Product('55 QLED 4K', 'Фоновая подсветка', 123000.0, 7)",
    "Product('Test', 'Test', 1000, 10)",
    "Smartphone('Test2', 'Test2', 2000, 10, 'Высокая', 'Модель', 256, 'Черный')",
    "LawnGrass('Test3', 'Test3', 3000, 10, 'Россия', 7, 'Зеленый')"
]

actual_output = [
                    repr(product) for product in category_smartphones._Category__products
                ] + [
                    repr(product) for product in category_products._Category__products
                ] + [
                    repr(product) for product in category_test._Category__products
                ]

print("Ожидаемый вывод продуктов:")
print("\n".join(expected_output))
print("Фактический вывод продуктов:")
print("\n".join(actual_output))

products_match = expected_output == actual_output
print(f"Вывод продуктов совпадает: {products_match}")

# Финальная проверка
final_check = products_match and price_comparison_result
print(f"Финальная проверка: {final_check}")
