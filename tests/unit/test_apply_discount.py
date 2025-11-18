from src.pricing import apply_discount
import pytest

@pytest.mark.parametrize("price,percent,expected", [
    (100.0, 10, 90.0),
    (50.0, 0, 50.0),
    (80.0, 100, 0.0),
])

def test_apply_discount(price, percent, expected):
    result = apply_discount(price, percent)
    assert result == pytest.approx(expected)

def test_apply_discount_negative_percent():
    with pytest.raises(ValueError):
        apply_discount(100.0, -5)