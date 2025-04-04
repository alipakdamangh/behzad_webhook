# test_factorial.py
from factorial import factorial

def test_factorial_of_5():
    assert factorial(5) == 120

def test_factorial_of_0():
    assert factorial(0) == 1
