""" Import Calculation Parent Class Constructor """

from calculator.calculator_calculations.calculation import Calculation

# This is division method which inherits the calculation class constructor


class Division(Calculation):
    """ Performs division between two values coming from Parent Class and gives the results """

    def getresult(self):
        """ Using self to reference the data contained in the object instance """
        division_of_values = self.values[0]
        for value in self.values[1:]:
            division_of_values = division_of_values / value
        return round(division_of_values, 3)
