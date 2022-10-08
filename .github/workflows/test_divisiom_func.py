from tests.utils import division
import pytest


@pytest.mark.parametrize("a,b,expected_result", [(10, 2, 5),
                                                 (20, 4, 5),
                                                 (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize("expected_exeption, divider, divisionable", [(ZeroDivisionError, 0, 10),
                                                                      (TypeError, "2", 20)])
def test_division_error(expected_exeption, divider, divisionable):
    with pytest.raises(expected_exeption):
        division(divisionable, divider)
