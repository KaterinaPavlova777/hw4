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
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        ["Samsung Galaxy S23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"],
    )


def test_category(category_smartphone: Category) -> None:
    assert category_smartphone.name == "Смартфоны"

    assert (
        category_smartphone.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_smartphone.products == ["Samsung Galaxy S23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"]


def test_category_count() -> None:
    Category.category_count = 0
    _ = Category("Категория 1", "Описание категории 1", [])
    _ = Category("Категория 2", "Описание категории 2", [1, 2, 3])

    assert Category.category_count == 2


def test_product_count() -> None:
    Category.category_count = 0
    _ = Category("Категория 1", "Описание категории 1", [])
    _ = Category("Категория 2", "Описание категории 2", [1, 2, 3])

    assert Category.product_count == 5
