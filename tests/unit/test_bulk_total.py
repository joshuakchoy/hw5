from src.pricing import bulk_total
import pytest

def test_bulk_total():
    prices = [10.00, 20.00, 30.00]
    total = bulk_total(prices, discount_percent=0, tax_rate=0.0)
    assert total == 60.00