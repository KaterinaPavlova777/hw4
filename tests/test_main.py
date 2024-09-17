import pytest

from src.main import Category, Product


@pytest.fixture
def product_samsung() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_product(product_samsung: Product) -> None:
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


@pytest.fixture
def category_smartphone() -> Category:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return Category("Electronics", "Electronic device", [product1, product2])


def test_category_init(category_smartphone: Category) -> None:
    assert category_smartphone.name == "Electronics"
    assert category_smartphone.description == "Electronic device"
    assert len(category_smartphone.products) == 2
    assert category_smartphone.category_count == 1
    assert category_smartphone.product_count == 2
