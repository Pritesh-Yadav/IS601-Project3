""" Import Calculation Parent Class Constructor """

from calculator.calculator_calculations.calculation import Calculation

# This is multiplication method which inherits the calculation class constructor


class Multiplication(Calculation):
    """ Performs multiply between two values coming from Parent Class and gives the results """

    def getresult(self):
        """ Using self to reference the data contained in the object instance """
        multiplication_of_values = 1
        for value in self.values:
            multiplication_of_values = multiplication_of_values * value
        return round(multiplication_of_values, 3)
