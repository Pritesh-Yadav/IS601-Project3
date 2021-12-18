"""Importing Calculator main.py for Testing"""
import pytest
from calculator.main import Calculator
from calculator.history_calculations.history_calculations import History

# pylint: disable=unused-argument,redefined-outer-name

num_1, num_2, add, sub, multi, div = Calculator('csv_handling/input/data.csv').get_data()
length = len(add)


# This is a fixture
@pytest.fixture
def clear_history():
    """ Clears history """
    History.clear_history()


def test_calculator_add(clear_history):
    """ To check if calculator addition result is correct """

    for i in range(length):
        assert Calculator.add_nums(num_1[i], num_2[i]) == add[i]
    assert History.get_calculation_count() == 6
    assert History.get_last_calculation_added() == add[-1]
    assert History.get_first_calculation_history() == add[0]


def test_calculator_subtract(clear_history):
    """ To check if calculator subtraction result is correct """
    for i in range(length):
        assert Calculator.subtract_nums(num_1[i], num_2[i]) == sub[i]


def test_calculator_multiply(clear_history):
    """ To check if calculator multiplication result is correct """
    for i in range(length):
        assert Calculator.multiply_nums(num_1[i], num_2[i]) == multi[i]


def test_calculator_divide(clear_history):
    """ To check if calculator division result is correct """
    for i in range(length):
        assert Calculator.divide_nums(num_1[i], num_2[i]) == div[i]
