import pytest
from app import calculate_factorial

def test_factorial_positive_numbers():
    assert calculate_factorial(5) == 120
    assert calculate_factorial(3) == 6
    assert calculate_factorial(10) == 3628800

def test_factorial_zero_and_one():
    assert calculate_factorial(0) == 1
    assert calculate_factorial(1) == 1

def test_factorial_negative_numbers():
    with pytest.raises(ValueError):
        calculate_factorial(-5)