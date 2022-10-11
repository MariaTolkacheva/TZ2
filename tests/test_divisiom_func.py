from functions import *
import pytest
import time
start_time = time.time()

@pytest.mark.parametrize("a,expected_result", [(['1', '2', '3', '3', '4'], 1),
                                               (['3', '2', '3', '3', '4'], 2),
                                               (['7', '8', '1000', '89898', '988'], 7), ])
# Testing min

def test_min_good(a, expected_result):
    assert num_min(a) == expected_result


@pytest.mark.parametrize("expected_exeption, a", [(ValueError, ['1', '3', '5', 'k'])])
def test_min_error(expected_exeption, a):
    with pytest.raises(expected_exeption):
        num_min(a)


# Testing max
@pytest.mark.parametrize("a,expected_result", [(['1', '2', '3', '3', '4'], 4),
                                               (['3', '2', '3', '3', '6'], 6),
                                               (['7', '8', '1000', '89898', '988'], 89898), ])
def test_max_good(a, expected_result):
    assert num_max(a) == expected_result


@pytest.mark.parametrize("expected_exeption, a", [(ValueError, ['1', '3', '5', 'k'])])
def test_max_error(expected_exeption, a):
    with pytest.raises(expected_exeption):
        num_max(a)


# Testing prod
@pytest.mark.parametrize("a,expected_result", [(['1', '2', '3', '3', '4'], 72),
                                               (['3', '2', '3', '3', '6'], 324),
                                               (['7', '8', '9', '10', '11'], 55440), ])
def test_prod_good(a, expected_result):
    assert num_prod(a) == expected_result


@pytest.mark.parametrize("expected_exeption, a", [(ValueError, ['1', '3', '5', 'k'])])
def test_prod_error(expected_exeption, a):
    with pytest.raises(expected_exeption):
        num_prod(a)
