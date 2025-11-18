from src.order_io import load_order
import pytest

def test_load_order_failure(tmp_path):
    with pytest.raises(ValueError, match="Malformed line: BadLine"):
        p = tmp_path / "bad_order.txt"
        p.write_text("Item1,$10.00\nBadLine\nItem2,$20.00\n")
        load_order(p)