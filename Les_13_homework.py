class Product:
    """
    Класс для описания товара в магазине
    """
    name: str
    description: str
    _price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, name, description, price, quantity):
        """
        Класс-метод для создания нового продукта
        """
        return cls(name, description, price, quantity)

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
    name: str
    description: str
    _products: list

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self._products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self._products)

    def add_product(self, product):
        """
        Метод для добавления продукта в категорию
        """
        if isinstance(product, Product):
            self._products.append(product)
            Category.product_count += 1
        else:
            print("Добавляемый объект должен быть экземпляром класса Product")

    @property
    def products(self):
        """
        Геттер для списка продуктов, возвращающий их в виде строки
        """
        return "\n".join([str(product) for product in self._products])

    def __str__(self):
        """
        Метод для представления объекта в виде строки
        """
        return f"Категория: {self.name}, Описание: {self.description}, Товаров: {len(self._products)}"


# Пример использования

# Создание продуктов
product1 = Product.new_product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product.new_product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product.new_product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
product4 = Product.new_product("55 QLED 4K", "Фоновая подсветка", 123000.0, 7)

# Создание категорий и добавление продуктов
category1 = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни")
category1.add_product(product1)
category1.add_product(product2)
category1.add_product(product3)

category2 = Category("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником")
category2.add_product(product4)

# Вывод информации о категориях и продуктах
for category in [category1, category2]:
    print(category)
    print(category.products)

print(f"Всего категорий: {Category.category_count}")
print(f"Всего продуктов: {Category.product_count}")
