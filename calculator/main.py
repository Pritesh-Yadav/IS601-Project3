""" import all the methods from calc_methods"""
from calculator.calculator_calculations.addition import Addition
from calculator.calculator_calculations.subtraction import Subtraction
from calculator.calculator_calculations.multiplication import Multiplication
from calculator.calculator_calculations.division import Division
from calculator.history_calculations.history_calculations import History


class Calculator:
    """ Creating a Module Calculator """
    # result set to 0 for initialization

    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        # I made this method so that I don't have more than one action per function
        print(History.get_last_calculation_added())
        return History.get_last_calculation_added()

    @staticmethod
    def addition(args: tuple):
        """ Adds given list of numbers and appends the result to history """
        print(History.add_addition_to_history(args))
        return History.add_addition_to_history(args)

    @staticmethod
    def subtraction(args: tuple):
        """ Subtracts given list of numbers and appends the result to history """

        return History.add_subtraction_to_history(args)


    @staticmethod
    def multiplication(args: tuple):
        """ Multiplies given list of numbers and appends the result to history """

        return History.add_multiplication_to_history(args)

    @staticmethod
    def division(args: tuple):
        """ Divides given list of numbers and appends the result to history """

        return History.add_division_to_history(args)
