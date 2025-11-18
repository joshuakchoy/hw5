from src.pricing import add_tax
import pytest

@pytest.mark.parametrize("price,tax_rate,expected", [
    (100.0, 0.1, 110.0),
    (200.0, 0.2, 240.0),
    (50.0, 0.0, 50.0),
    (80.0, 0.15, 92.0),
])

def test_add_tax(price, tax_rate, expected):
    result = add_tax(price, tax_rate)
    assert result == pytest.approx(expected)

def test_add_tax_negative_rate():
    with pytest.raises(ValueError):
        add_tax(100.0, -0.05)