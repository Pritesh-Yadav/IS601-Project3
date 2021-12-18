""" Import Calculation Parent Class Constructor """
from calculator.calculator_calculations.calculation import Calculation
# This is addition method which inherits the calculation class constructor


class Addition(Calculation):
    """ Performs addition between two values coming from Parent Class and gives the results """

    def getresult(self):
        """ Using self to reference the data contained in the object instance """
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = sum_of_values + value
        return round(sum_of_values, 3)
