from src.pricing import bulk_total
from src.order_io import *
import pytest


def test_integration(tmp_path):
    input_file = tmp_path / "sample_order.csv"
    input_file.write_text("chicken,$10.00\nbeef,$15.00\n")

    items = load_order(input_file)

    prices = [item[1] for item in items]
    total = bulk_total(prices)
    
    write_receipt(tmp_path / "sample_receipt.csv", items)

    output_file = tmp_path / "sample_receipt.csv"
    assert "chicken: $10.00" in output_file.read_text()
    assert "TOTAL: " in output_file.read_text()