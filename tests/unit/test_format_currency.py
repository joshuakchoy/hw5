from src.pricing import format_currency
import pytest

@pytest.mark.parametrize("input_value,expected", [
    (1234.5, "$1234.50"),
    (12.5, "$12.50"),
    (0.99, "$0.99"),
    (1000, "$1000.00"),
])

def test_format_currency(input_value, expected):
    assert format_currency(input_value) == expected