from src.pricing import parse_price
import pytest

@pytest.mark.parametrize("input_text,expected", [
    ("$1,234.50", 1234.50),
    ("12.5", 12.5),
    ("$0.99", 0.99),
    ("1000", 1000.0),
])

def test_parse_price(input_text, expected):
    assert parse_price(input_text) == expected