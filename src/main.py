from typing import Any


class Product:
    """
    Класс для представления продукта.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Метод для инициализации экземпляра класса.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_products: dict) -> Any:
        """
        Метод, который возвращает созданный объект класса Product.
        """
        new_dict_products = cls(
            dict_products["name"], dict_products["description"], dict_products["price"], dict_products["quantity"]
        )
        return new_dict_products

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> Any:
        if price > 0:
            self.__price = price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Category:
    """
    Класс для представления категории.
    """

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """
        Метод для инициализации экземпляра класса.
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """
        Метод для добавления продуктов в категории.
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Метод для вывода списка товаров.
        """
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str
