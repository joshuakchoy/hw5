from src.pricing import bulk_total
import pytest

@pytest.mark.parametrize("prices,discount_percent,tax_rate,expected", [
    ([10.00, 20.00, 30.00], 0, 0.0, 60.00), 
    ([10.00, 20.00, 30.00], 10, 0.0, 54.00),
    ([10.00, 20.00, 30.00], 0, 0.07, 64.20),
])

def test_bulk_total(prices, discount_percent, tax_rate, expected):
    total = bulk_total(prices, discount_percent=discount_percent, tax_rate=tax_rate)
    assert total == pytest.approx(expected)