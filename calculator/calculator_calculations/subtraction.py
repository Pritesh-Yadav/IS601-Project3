""" Import Calculation Parent Class Constructor """

from calculator.calculator_calculations.calculation import Calculation

# This is subtraction method which inherits the calculation class constructor


class Subtraction(Calculation):
    """ Performs subtraction between two values coming from Parent Class and gives the results """

    def getresult(self):
        """ Using self to reference the data contained in the object instance """
        subtraction_of_values = self.values[0]
        for value in self.values[1:]:
            subtraction_of_values = subtraction_of_values - value
        return round(subtraction_of_values, 3)
