from utils import division
import pytest


@pytest.mark.parametrize("a,b,expected_result", [(10, 2, 5),
                                                 (20, 4, 5),
                                                 (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a,b) == expected_result
