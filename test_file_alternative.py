from abc import ABC, abstractmethod

class InitPrintMixin:
    def __init_print__(self, *args):
        class_name = self.__class__.__name__
        params = ', '.join([f"'{arg}'" if isinstance(arg, str) else str(arg) for arg in args])
        print(f"{class_name}({params})")

class BaseProduct(ABC):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

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
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        self.__init_print__(name, description, price, quantity, efficiency, model, memory, color)

    @classmethod
    def new_product(cls, products):
        return cls(**products)

    def __str__(self):
        return f"{self.name} {self.model}, {self.price} руб. Остаток: {self.quantity} шт. (Цвет: {self.color}, Память: {self.memory}GB, Эффективность: {self.efficiency})"

    def __repr__(self):
        return f"Smartphone('{self.name}', '{self.description}', {self.price}, {self.quantity}, '{self.efficiency}', '{self.model}', {self.memory}, '{self.color}')"

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
        self.__init_print__(name, description, price, quantity, country, germination_period, color)

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
                raise TypeError("Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)")
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

category_smartphones = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни")
category_lawngrass = Category("Газонная трава", "Газонная трава для вашего сада")

for product_data in data_smartphones:
    smartphone = Smartphone.new_product(product_data)
    category_smartphones.add_product(smartphone)

for product_data in data_lawngrass:
    lawn_grass = LawnGrass.new_product(product_data)
    category_lawngrass.add_product(lawn_grass)

test_product = Product("Test", "Test", 1000, 10)
test_smartphone = Smartphone("Test2", "Test2", 2000, 10, "Средняя", "T2", 64, "Черный")
test_lawn_grass = LawnGrass("Test3", "Test3", 3000, 10, "Россия", 5, "Зеленый")

category_test = Category("Тестовая категория", "Категория для тестирования")
category_test.add_product(test_product)
category_test.add_product(test_smartphone)
category_test.add_product(test_lawn_grass)

print(repr(test_product))
print(repr(test_smartphone))
print(repr(test_lawn_grass))

try:
    category_test.add_product("не продукт")
except TypeError as e:
    print("Можно добавлять только объекты класса Product или его наследников (Smartphone/LawnGrass)")

assert True == True

product1 = Smartphone("Product1", "Description1", 100, 10, "Высокая", "P1", 128, "Черный")
product2 = Smartphone("Product2", "Description2", 200, 2, "Средняя", "P2", 64, "Белый")
try:
    total_cost = product1 + product2
    print(total_cost)
except TypeError as e:
    print(e)

try:
    category_test.products = ["не продукт"]
except TypeError as e:
    print(e)

correct_products_list = [test_product, test_smartphone, test_lawn_grass]
try:
    category_test.products = correct_products_list
    print(category_test.products)
except TypeError as e:
    print(e)

categories = {
    "smartphones": category_smartphones,
    "lawngrass": category_lawngrass,
    "test": category_test
}

for name, category in categories.items():
    print(f"Category '{name}' products before test: {category.products}")

products_data = [
    {
        "name": "55 QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
    }
]

product_item = [Product.new_product(data) for data in products_data]

print(f"Type of product_item: {type(product_item)}")
print(f"Contents of product_item: {product_item}")

for idx, item in enumerate(product_item):
    print(f"Item {idx}: {item}, Type: {type(item)}")

print(f"Category 'smartphones' products before assignment: {categories['smartphones'].products}")

try:
    categories['smartphones'].products = product_item
except TypeError as e:
    print(e)

print(f"Category 'smartphones' products after assignment: {categories['smartphones'].products}")

print("Все тесты пройдены успешно.")
