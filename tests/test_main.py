from typing import Any

import pytest

from src.main import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def product_samsung() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                   180000.0, 5)


def test_product(product_samsung: Product) -> None:
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


@pytest.fixture
def category_smartphone() -> Category:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                       180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return Category("Electronics", "Electronic device", [product1, product2])


def test_category_init(category_smartphone: Category) -> None:
    assert category_smartphone.name == "Electronics"
    assert category_smartphone.description == "Electronic device"
    # assert len(category_smartphone.__products) == 2
    assert category_smartphone.category_count == 1
    assert category_smartphone.product_count == 2


def test_new_product() -> None:
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.description == "256GB, Серый цвет, 200MP камера"


def test_price_setter() -> None:
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    new_product.price = -100000.0
    assert new_product.price == 180000.0


def test_category_add() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                       180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций "
        "для удобства жизни",
        [product1, product2, product3],
    )
    assert category1.product_count == 5
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    assert category1.product_count == 6


def test_category_str() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
                       5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций"
        " для удобства жизни",
        [product1, product2, product3],
    )
    assert str(category1) == "Смартфоны, количество продуктов: 27 шт."


def test_product_str() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
                       5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product2) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_product_add() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
                       5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    assert (product1.price * product1.quantity) + (product2.price * product2.quantity) == 2580000


@pytest.fixture
def smartphone1() -> Smartphone:
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
        180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone2() -> Smartphone:
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0,
                      8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawn_grass1() -> LawnGrass:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0,
                     20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass2() -> LawnGrass:
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0,
                     15, "США", "5 дней", "Темно-зеленый")


def test_add_smartphone(category_smartphone: Any, smartphone1: Smartphone) -> None:
    category_smartphone.add_product = smartphone1


def test_add_error(category_smartphone: Any) -> None:
    with pytest.raises(TypeError):
        category_smartphone.add_product(1)


def test_lawn_grass(lawn_grass1: Any, lawn_grass2: Any) -> None:
    assert lawn_grass1.name == "Газонная трава"
    assert lawn_grass1.description == "Элитная трава для газона"
    assert lawn_grass1.price == 500.0
    assert lawn_grass1.quantity == 20
    assert lawn_grass1.country == "Россия"
    assert lawn_grass1.germination_period == "7 дней"
    assert lawn_grass1.color == "Зеленый"

    assert lawn_grass2.name == "Газонная трава 2"
    assert lawn_grass2.description == "Выносливая трава"
    assert lawn_grass2.price == 450.0
    assert lawn_grass2.quantity == 15
    assert lawn_grass2.country == "США"
    assert lawn_grass2.germination_period == "5 дней"
    assert lawn_grass2.color == "Темно-зеленый"


def test_add_lawn_grass(lawn_grass1: Any, lawn_grass2: Any) -> None:
    assert lawn_grass1 + lawn_grass2 == 16750.0
