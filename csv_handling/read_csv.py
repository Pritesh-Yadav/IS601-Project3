""" CSV Read Class """

import pandas as pd


class CSVRead:
    """ Defining Class Constructor in here """

    # pylint: disable=too-few-public-methods

    @staticmethod
    def read_data(path):
        """ Returns the data from the csv file """
        return pd.read_csv(path)
