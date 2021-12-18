
""" import all the methods from calc_methods"""
from calculator.calculator_calculations.addition import Addition
from calculator.calculator_calculations.subtraction import Subtraction
from calculator.calculator_calculations.multiplication import Multiplication
from calculator.calculator_calculations.division import Division


class History:
    """ Creating a Module Calculator """
    # result set to 0 for initialization
    history = []

    @staticmethod
    def clear_history():
        """ Clear the history array """
        History.history.clear()

    @staticmethod
    def add_calculation_to_history(calculation):
        """ Appends calculation to history array """
        History.history.append(calculation)

    @staticmethod
    def get_first_calculation_history():
        """ Gets first calculation from history array """
        return History.history[0]

    @staticmethod
    def get_last_calculation_added():
        """ Gets last calculation from history array """
        return History.history[-1]

    @staticmethod
    def get_calculation_count():
        """ Gets number of calculations from history array """
        return len(History.history)

    @staticmethod
    def add_addition_to_history(values):
        """ Adds addition to history """
        return History.add_calculation_to_history(Addition.create(values).getresult())

    @staticmethod
    def add_subtraction_to_history(values):
        """ Adds subtraction to history """
        return History.add_calculation_to_history(Subtraction.create(values).getresult())

    @staticmethod
    def add_multiplication_to_history(values):
        """ Adds multiplication to history """
        return History.add_calculation_to_history(Multiplication.create(values).getresult())

    @staticmethod
    def add_division_to_history(values):
        """ Adds division to history """
        return History.add_calculation_to_history(Division.create(values).getresult())
