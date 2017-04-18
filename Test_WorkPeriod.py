#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Mar - Apr 2017

@author: Tommy Cusack
"""

# import Python libraries
import datetime as datetime
# import numpy as np
# import os
import unittest

# from datetime import timedelta

import WorkPeriod as WorkPeriod


class Test_WorkPeriod(unittest.TestCase):
    """ Basic Unit test class for Trade

    @author: Tommy Cusack

    Any method starting with ``test_`` will considered as a test case."""

    # defs defined by unittest
    @classmethod
    def setUpClass(cls):
        """ unittest method: setUp variables for unit tests to run"""

        cls.WorkPeriod = WorkPeriod.WorkPeriod()

    def suite():
        """ unittest method: returns a collected suite of tests"""

        suite = unittest.TestLoader().loadTestsFromTestCase(Test_WorkPeriod)
        return suite


    @classmethod
    def tearDownClass(cls):
        """ unittest method: dispose of setUpClass variables that unit tests hooked onto"""
        # self.dataFormatAnalyser.dispose()
        cls.WorkPeriod = None


    # developer defined defs begin
    def test_is_calculate_settlement_date_consistent_aed(cls):
        """
        Tests WorkPeriod.WorkPeriod.calculate_settlement_date().

        WorkPeriod.calculate_settlement_date() is greater than or equal to passed settlement_date.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """
        currency = "AED"
        settlement_date_date = datetime.date(2001, 1, 13)

        cls.assertEqual(True, (
        cls.WorkPeriod.calculate_settlement_date(currency, settlement_date_date) >= settlement_date_date))

    def test_is_calculate_settlement_date_consistent_sar(cls):
        """
        Tests WorkPeriod.WorkPeriod.calculate_settlement_date().

        WorkPeriod.calculate_settlement_date() is greater than or equal to passed settlement_date.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """
        currency = "SAR"
        settlement_date_date = datetime.date(2001, 1, 13)

        cls.assertEqual(True, (
        cls.WorkPeriod.calculate_settlement_date(currency, settlement_date_date) >= settlement_date_date))

    def test_is_calculate_settlement_date_consistent_sgp(cls):
        """
        Tests WorkPeriod.WorkPeriod.calculate_settlement_date().

        WorkPeriod.calculate_settlement_date() is greater than or equal to passed settlement_date.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """
        currency = "SGP"
        settlement_date_date = datetime.date(2001, 1, 13)

        cls.assertEqual(True, (
        cls.WorkPeriod.calculate_settlement_date(currency, settlement_date_date) >= settlement_date_date))


    def test_is_day_of_work_period_valid_too_small(cls):
        """
        Tests WorkPeriod.WorkPeriod.is_day_of_work_period_valid().

        WorkPeriod.is_day_of_work_period_valid() is passed an int less than permitted minimum.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.WorkPeriod.is_day_of_work_period_valid(WorkPeriod.DAY_OF_WORK_PERIOD_MINIMUM - 1))

    def test_is_day_of_work_period_valid_too_big(cls):
        """
        Tests WorkPeriod.WorkPeriod.is_day_of_work_period_valid().

        WorkPeriod.is_day_of_work_period_valid() is passed an int less than permitted minimum.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.WorkPeriod.is_day_of_work_period_valid(WorkPeriod.DAY_OF_WORK_PERIOD_MAXIMUM + 1))


    def test_is_currency_valid_wrong_currency(cls):
        """
        Tests WorkPeriod.WorkPeriod.is_currency_valid().

        WorkPeriod.is_currency_valid() is passed the wrong currency.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.WorkPeriod.is_currency_valid("wrong currency"))


    def test_is_currency_valid_wrong_currency_wrong_case(cls):
        """
        Tests WorkPeriod.WorkPeriod.is_currency_valid().

        WorkPeriod.is_currency_valid() is passed the wrong currency in the wrong case.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.WorkPeriod.is_currency_valid("aed"))


    def test_is_variables_internally_consistent(cls):
        """
        Tests len(WorkPeriod.CURRENCIES) = len(WorkPeriod.WORK_PERIODS)

        CURRENCIES and WORK_PERIODS must always be the same size

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(True, (len(WorkPeriod.CURRENCIES) == len(WorkPeriod.WORK_PERIODS)))

    def test_is_variables_internally_consistent_maximum_gretarer_than_minimum(cls):
        """
        Tests WorkPeriod.DAY_OF_WORK_PERIOD_MAXIMUM >= WorkPeriod.DAY_OF_WORK_PERIOD_MINIMUM

        WorkPeriod.DAY_OF_WORK_PERIOD_MAXIMUM must always be >= WorkPeriod.DAY_OF_WORK_PERIOD_MINIMUM

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(True, (WorkPeriod.DAY_OF_WORK_PERIOD_MAXIMUM >= WorkPeriod.DAY_OF_WORK_PERIOD_MINIMUM))

    if __name__ == '__main__':
        unittest.main()