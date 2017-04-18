#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Mar - Apr 2017

@author: Tommy Cusack
"""

# import Python libraries
import datetime as datetime
import decimal as decimal
import numpy as np
# import os
import unittest

from datetime import timedelta

import Trade as Trade

class Test_Trade(unittest.TestCase):  # (object)
    """ Basic Unit test class for Trade

    @author: Tommy Cusack

    Any method starting with ``test_`` will considered as a test case."""

    # defs defined by unittest
    @classmethod
    def setUpClass(cls):
        """ unittest method: setUp variables for unit tests to run"""
        agreed_fx_decimal = decimal.Decimal('12.34')
        buy_sell_string = "B"
        currency_string = "zln"
        entity_string = "ent"
        instruction_date_datetime = datetime.datetime(2016, 1, 1, 0, 0, 0)
        price_per_unit_decimal = decimal.Decimal('3.14')
        SETTLEMENT_DATE_DATE = datetime.datetime(2016, 1, 5, 0, 0, 0)
        units = 100

        cls.Trade = Trade.Trade(agreed_fx_decimal, buy_sell_string
                                , currency_string, entity_string, instruction_date_datetime
                                , price_per_unit_decimal, SETTLEMENT_DATE_DATE, units)

    def suite():
        """ unittest method: returns a collected suite of tests"""

        suite = unittest.TestLoader().loadTestsFromTestCase(Test_Trade)
        return suite

    @classmethod
    def tearDownClass(cls):
        """ unittest method: dispose of setUpClass variables that unit tests hooked onto"""
        # self.dataFormatAnalyser.dispose()
        cls.Trade = None

    # developer defined defs begin
    def test_is_agreed_fx_data_valid_float(cls):
        """
        Tests Trade.Trade.is_agreed_fx_data_valid().

        Trade.is_agreed_fx_data_valid() is passed a float instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        # res = self.Trade.Trade.is_agreed_fx_data_valid()
        cls.assertEqual(False, cls.Trade.is_agreed_fx_data_valid(3.4))

    def test_is_agreed_fx_data_valid_infinity_numpy(cls):
        """
        Tests Trade.Trade.is_agreed_fx_data_valid().

        Trade.is_agreed_fx_data_valid() is passed infinity instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        # res = self.Trade.Trade.is_agreed_fx_data_valid()
        cls.assertEqual(False, cls.Trade.is_agreed_fx_data_valid(np.inf))

    def test_is_agreed_fx_data_valid_less_than_zero(cls):
        """
        Tests Trade.Trade.is_agreed_fx_data_valid().

        Trade.is_agreed_fx_data_valid() is passed a Decimal less than zero.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """
        # res = self.Trade.Trade.is_agreed_fx_data_valid()
        cls.assertEqual(False, cls.Trade.is_agreed_fx_data_valid(-1))

    def test_is_agreed_fx_data_valid_minus_zero(cls):
        """
        Tests Trade.Trade.is_agreed_fx_data_valid().

        Trade.is_agreed_fx_data_valid() is passed a Decimal (= minus zero) testing
        lowest permitted bounds.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """
        # res = self.Trade.Trade.is_agreed_fx_data_valid()
        cls.assertEqual(False, cls.Trade.is_agreed_fx_data_valid(-0))

    def test_is_agreed_fx_data_valid_negative_infinity_numpy(cls):
        """
        Tests Trade.Trade.is_agreed_fx_data_valid().

        Trade.is_agreed_fx_data_valid() is passed negative infinity
        instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        # res = self.Trade.Trade.is_agreed_fx_data_valid()
        cls.assertEqual(False, cls.Trade.is_agreed_fx_data_valid(np.NINF))

    def test_is_agreed_fx_data_valid_none(cls):
        """
        Tests Trade.Trade.is_agreed_fx_data_valid().

        Trade.is_agreed_fx_data_valid() is passed None instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        # res = self.Trade.Trade.is_agreed_fx_data_valid()
        cls.assertEqual(False, cls.Trade.is_agreed_fx_data_valid(None))

    def test_is_agreed_fx_data_valid_not_a_number_numpy(cls):
        """
        Tests Trade.Trade.is_agreed_fx_data_valid().

        Trade.is_agreed_fx_data_valid() is passed nan(Not A Number)
        instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        # res = self.Trade.Trade.is_agreed_fx_data_valid()
        cls.assertEqual(False, cls.Trade.is_agreed_fx_data_valid(np.nan))

    def test_is_agreed_fx_data_valid_plus_number_minus_bigger_number(cls):
        """
        Tests Trade.Trade.is_agreed_fx_data_valid().

        Trade.is_agreed_fx_data_valid() is passed a compound argument (adding 2
        numbers together) instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        # res = self.Trade.Trade.is_agreed_fx_data_valid()
        cls.assertEqual(False, cls.Trade.is_agreed_fx_data_valid(+ 1 - 2))

    def test_is_argument_name_valid_boolean(cls):
        """
        Tests Trade.Trade.is_argument_name_valid().

        Trade.is_argument_name_valid() passed int instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_argument_name_valid(False))

    def test_is_argument_name_valid_integer(cls):
        """
        Tests Trade.Trade.is_argument_name_valid().

        Trade.is_argument_name_valid() passed int instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_argument_name_valid(666))

    def test_is_argument_name_valid_float(cls):
        """
        Tests Trade.Trade.is_argument_name_valid().

        Trade.is_argument_name_valid() passed float instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_argument_name_valid(66.6))

    def test_is_argument_name_valid_none(cls):
        """
        Tests Trade.Trade.is_argument_name_valid().

        Trade.is_argument_name_valid() passed None instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_argument_name_valid(None))

    def test_is_argument_name_valid_nothing(cls):
        """
        Tests Trade.Trade.is_argument_name_valid().

        Trade.is_argument_name_valid() passed nothing instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_argument_name_valid(""))

    def test_is_argument_name_valid_not_alphanumeric(cls):
        """
        Tests Trade.Trade.is_argument_name_valid().

        Trade.is_argument_name_valid() passed a non-alphanumeric string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_argument_name_valid("12.3"))

    def test_is_argument_name_valid_not_alphanumeric_2(cls):
        """
        Tests Trade.Trade.is_argument_name_valid().

        Trade.is_argument_name_valid() passed a non-alphanumeric string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_argument_name_valid("ab/3"))

    def test_is_argument_name_valid_not_alphanumeric_3(cls):
        """
        Tests Trade.Trade.is_argument_name_valid().

        Trade.is_argument_name_valid() passed a non-alphanumeric string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_argument_name_valid("a/+*-b."))

    def test_is_argument_name_valid_not_alphanumeric_4(cls):
        """
        Tests Trade.Trade.is_argument_name_valid().

        Trade.is_argument_name_valid() passed a non-alphanumeric string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_argument_name_valid("ab?$"))

    def test_is_argument_name_valid_not_a_number(cls):
        """
        Tests Trade.Trade.is_argument_name_valid().

        Trade.is_argument_name_valid() passed not a number instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_argument_name_valid(np.nan))

    def test_is_argument_name_valid_too_short(cls):
        """
        Tests Trade.Trade.is_argument_name_valid().

        Trade.is_argument_name_valid() passed a too short string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_argument_name_valid("___"))

    def test_is_buy_sell_data_valid_boolean(cls):
        """
        Tests Trade.Trade.is_buy_sell_data_valid().

        Trade.is_buy_sell_data_valid() passed int instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_buy_sell_data_valid(False))

    def test_is_buy_sell_data_valid_integer(cls):
        """
        Tests Trade.Trade.is_buy_sell_data_valid().

        Trade.is_buy_sell_data_valid() passed int instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_buy_sell_data_valid(666))

    def test_is_buy_sell_data_valid_float(cls):
        """
        Tests Trade.Trade.is_buy_sell_data_valid().

        Trade.is_buy_sell_data_valid() passed float instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_buy_sell_data_valid(66.6))

    def test_is_buy_sell_data_valid_none(cls):
        """
        Tests Trade.Trade.is_buy_sell_data_valid().

        Trade.is_buy_sell_data_valid() passed None instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_buy_sell_data_valid(None))

    def test_is_buy_sell_data_valid_nothing(cls):
        """
        Tests Trade.Trade.is_buy_sell_data_valid().

        Trade.is_buy_sell_data_valid() passed nothing instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_buy_sell_data_valid(""))

    def test_is_buy_sell_data_valid_not_alphabetic(cls):
        """
        Tests Trade.Trade.is_buy_sell_data_valid().

        Trade.is_buy_sell_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_buy_sell_data_valid("1"))

    def test_is_buy_sell_data_valid_not_alphabetic_2(cls):
        """
        Tests Trade.Trade.is_buy_sell_data_valid().

        Trade.is_buy_sell_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_buy_sell_data_valid("."))

    def test_is_buy_sell_data_valid_not_alphabetic_3(cls):
        """
        Tests Trade.Trade.is_buy_sell_data_valid().

        Trade.is_buy_sell_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_buy_sell_data_valid("_"))

    def test_is_buy_sell_data_valid_not_alphabetic_4(cls):
        """
        Tests Trade.Trade.is_buy_sell_data_valid().

        Trade.is_buy_sell_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_buy_sell_data_valid("$"))

    def test_is_buy_sell_data_valid_not_a_number(cls):
        """
        Tests Trade.Trade.is_buy_sell_data_valid().

        Trade.is_buy_sell_data_valid() passed not a number instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_buy_sell_data_valid(np.nan))

    def test_is_buy_sell_data_valid_too_long(cls):
        """
        Tests Trade.Trade.is_buy_sell_data_valid().

        Trade.is_buy_sell_data_valid() passed a too long string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_buy_sell_data_valid("BbBb"))

    def test_is_buy_sell_data_valid_correct_input_1(cls):
        """
        Tests Trade.Trade.is_buy_sell_data_valid().

        Trade.is_buy_sell_data_valid() passed a too short string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(True, cls.Trade.is_buy_sell_data_valid("B"))

    def test_is_buy_sell_data_valid_correct_input_2(cls):
        """
        Tests Trade.Trade.is_buy_sell_data_valid().

        Trade.is_buy_sell_data_valid() passed a too short string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(True, cls.Trade.is_buy_sell_data_valid("S"))

    def test_is_currency_data_valid_float(cls):
        """
        Tests Trade.Trade.is_currency_data_valid().

        Trade.is_currency_data_valid() passed float instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_currency_data_valid(66.6))

    def test_is_currency_data_valid_integer(cls):
        """
        Tests Trade.Trade.is_currency_data_valid().

        Trade.is_currency_data_valid() passed int instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_currency_data_valid(666))

    def test_is_currency_data_valid_none(cls):
        """
        Tests Trade.Trade.is_currency_data_valid().

        Trade.is_currency_data_valid() passed None instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_currency_data_valid(None))

    def test_is_currency_data_valid_nothing(cls):
        """
        Tests Trade.Trade.test_is_currency_data_valid().

        Trade.is_currency_data_valid() passed nothing instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_currency_data_valid(""))

    def test_is_currency_data_valid_not_alphabetic(cls):
        """
        Tests Trade.Trade.is_currency_data_valid().

        Trade.is_currency_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_currency_data_valid("123"))

    def test_is_currency_data_valid_not_alphabetic_2(cls):
        """
        Tests Trade.Trade.is_currency_data_valid().

        Trade.is_currency_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_currency_data_valid("ab3"))

    def test_is_currency_data_valid_not_alphabetic_3(cls):
        """
        Tests Trade.Trade.is_currency_data_valid().

        Trade.is_currency_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_currency_data_valid("ab."))

    def test_is_currency_data_valid_not_alphabetic_4(cls):
        """
        Tests Trade.Trade.is_currency_data_valid().

        Trade.is_currency_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_currency_data_valid("ab$"))

    def test_is_currency_data_valid_not_a_number(cls):
        """
        Tests Trade.Trade.is_currency_data_valid().

        Trade.is_currency_data_valid() passed not a number instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_currency_data_valid(np.nan))

    def test_is_currency_data_valid_too_long(cls):
        """
        Tests Trade.Trade.is_currency_data_valid().

        Trade.is_currency_data_valid() passed a too long string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_currency_data_valid("abcd"))

    def test_is_currency_data_valid_too_short(cls):
        """
        Tests Trade.Trade.is_currency_data_valid().

        Trade.is_currency_data_valid() passed a too short string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_currency_data_valid("12"))

    def test_is_date_valid_integer(cls):
        """
        Tests Trade.Trade.is_datetime_valid().

        Trade.is_datetime_valid() passed int instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_date_valid(666
                                                  , Trade.SETTLEMENT_DATE_DATE))

    def test_is_date_valid_float(cls):
        """
        Tests Trade.Trade.is_datetime_valid().

        Trade.is_datetime_valid() passed float instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_date_valid(66.6
                                                  , Trade.SETTLEMENT_DATE_DATE))

    def test_is_date_valid_none(cls):
        """
        Tests Trade.Trade.is_datetime_valid().

        Trade.is_datetime_valid() passed None instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_date_valid(None
                                                  , Trade.SETTLEMENT_DATE_DATE))

    def test_is_date_valid_nothing(cls):
        """
        Tests Trade.Trade.is_datetime_valid().

        Trade.is_datetime_valid() passed nothing instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False
                        , cls.Trade.is_date_valid(""
                                                  , Trade.SETTLEMENT_DATE_DATE))

    def test_is_date_valid_alphabetic(cls):
        """
        Tests Trade.Trade.is_datetime_valid().

        Trade.is_datetime_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_date_valid("123"
                                                  , Trade.SETTLEMENT_DATE_DATE))

    def test_is_date_valid_not_a_number(cls):
        """
        Tests Trade.Trade.is_datetime_valid().

        Trade.is_datetime_valid() passed not a number instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_date_valid(np.nan, Trade.SETTLEMENT_DATE_DATE))

    def test_is_date_valid_too_early(cls):
        """
        Tests Trade.Trade.is_datetime_valid().

        Trade.is_datetime_valid() passed not a number instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_date_valid(np.nan
                                                  , Trade.TRADE_DATE_EARLIEST - timedelta(microseconds=1)))

    def test_is_entity_data_valid_float(cls):
        """
        Tests Trade.Trade.is_entity_data_valid().

        Trade.is_entity_data_valid() passed float instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_entity_data_valid(66.6))

    def test_is_entity_data_valid_integer(cls):
        """
        Tests Trade.Trade.is_entity_data_valid().

        Trade.is_entity_data_valid() passed int instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_entity_data_valid(666))

    def test_is_entity_data_valid_none(cls):
        """
        Tests Trade.Trade.is_entity_data_valid().

        Trade.is_entity_data_valid() passed None instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_entity_data_valid(None))

    def test_is_entity_data_valid_nothing(cls):
        """
        Tests Trade.Trade.is_entity_data_valid().

        Trade.is_entity_data_valid() passed nothing instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_entity_data_valid(""))

    def test_is_entity_data_valid_not_alphabetic(cls):
        """
        Tests Trade.Trade.is_entity_data_valid().

        Trade.is_entity_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_entity_data_valid("123"))

    def test_is_entity_data_valid_not_alphabetic_2(cls):
        """
        Tests Trade.Trade.is_entity_data_valid().

        Trade.is_entity_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_entity_data_valid("ab3"))

    def test_is_entity_data_valid_not_alphabetic_3(cls):
        """
        Tests Trade.Trade.is_entity_data_valid().

        Trade.is_entity_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_entity_data_valid("ab."))

    def test_is_entity_data_valid_not_alphabetic_4(cls):
        """
        Tests Trade.Trade.is_entity_data_valid().

        Trade.is_entity_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_entity_data_valid("ab$"))

    def test_is_entity_data_valid_not_a_number(cls):
        """
        Tests Trade.Trade.is_entity_data_valid().

        Trade.is_entity_data_valid() passed not a number instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_entity_data_valid(np.nan))

    def test_is_entity_data_valid_too_long(cls):
        """
        Tests Trade.Trade.is_entity_data_valid().

        Trade.is_entity_data_valid() passed a too long string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_entity_data_valid("abcd"))

    def test_is_entity_data_valid_too_short(cls):
        """
        Tests Trade.Trade.is_entity_data_valid().

        Trade.is_entity_data_valid() passed a too short string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_entity_data_valid("12"))

    def test_is_instruction_and_settlement_dates_data_valid_too_early(cls):
        """
        Tests Trade.Trade.is_instruction_and_settlement_dates_data_valid().

        Trade.is_instruction_and_settlement_dates_data_valid() passed instruction_date_datetime >= SETTLEMENT_DATE_DATE instead of instruction_date_datetime <= SETTLEMENT_DATE_DATE.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        instruction_date_date = datetime.datetime(3017, 1, 1)
        settlement_date_date = instruction_date_date - timedelta(days=1)

        cls.assertEqual(False
                        , cls.Trade.is_instruction_and_settlement_dates_data_valid(
                instruction_date_date, settlement_date_date))

    def test_is_instruction_and_settlement_dates_data_valid_correct_inputs(cls):
        """
        Tests Trade.Trade.is_instruction_and_settlement_dates_data_valid().

        Trade.is_instruction_and_settlement_dates_data_valid() passed instruction_date_datetime >= SETTLEMENT_DATE_DATE instead of instruction_date_datetime <= SETTLEMENT_DATE_DATE.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        instruction_date_date = datetime.date(3017, 1, 1)
        settlement_date_date = instruction_date_date + timedelta(days=+100)

        cls.assertEqual(True
                        , cls.Trade.is_instruction_and_settlement_dates_data_valid(
                instruction_date_date, settlement_date_date))

    def test_is_instruction_date_data_valid_integer(cls):
        """
        Tests Trade.Trade.is_instruction_date_data_valid().

        Trade.is_instruction_date_data_valid() passed int instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_instruction_date_data_valid(666))

    def test_is_instruction_date_data_valid_float(cls):
        """
        Tests Trade.Trade.is_instruction_date_data_valid().

        Trade.is_instruction_date_data_valid() passed float instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_instruction_date_data_valid(66.6))

    def test_is_instruction_date_data_valid_none(cls):
        """
        Tests Trade.Trade.is_instruction_date_data_valid().

        Trade.is_instruction_date_data_valid() passed None instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_instruction_date_data_valid(None))

    def test_is_instruction_date_data_valid_nothing(cls):
        """
        Tests Trade.Trade.is_instruction_date_data_valid().

        Trade.is_instruction_date_data_valid() passed nothing instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False
                        , cls.Trade.is_instruction_date_data_valid(""))

    def test_is_instruction_date_data_valid_alphabetic(cls):
        """
        Tests Trade.Trade.is_instruction_date_data_valid().

        Trade.is_instruction_date_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_instruction_date_data_valid("123"))

    def test_is_instruction_date_data_valid_not_a_number(cls):
        """
        Tests Trade.Trade.is_instruction_date_data_valid().

        Trade.is_instruction_date_data_valid() passed not a number instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_instruction_date_data_valid(np.nan))

    def test_is_instruction_date_data_valid_too_early(cls):
        """
        Tests Trade.Trade.is_instruction_date_data_valid().

        Trade.is_instruction_date_data_valid() passed not a number instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_instruction_date_data_valid(Trade.TRADE_DATE_EARLIEST - timedelta(days=1)))

    def test_is_integer_data_valid_cannot_be_zero_float(cls):
        """
        Tests Trade.Trade.is_integer_data_valid().

        Trade.is_integer_data_valid() is passed a float instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_integer_data_valid(3.4, False))

    def test_is_integer_data_valid_cannot_be_zero_infinity_numpy(cls):
        """
        Tests Trade.Trade.is_integer_data_valid().

        Trade.is_integer_data_valid() is passed infinity instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_integer_data_valid(np.inf, False))

    def test_is_integer_data_valid_cannot_be_zero_less_than_zero(cls):
        """
        Tests Trade.Trade.is_integer_data_valid().

        Trade.is_integer_data_valid() is passed an int less than zero.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_integer_data_valid(-1, False))

    def test_is_integer_data_valid_cannot_be_zero_minus_zero(cls):
        """
        Tests Trade.Trade.is_integer_data_valid().

        Trade.is_integer_data_valid() is passed an int (= minus zero) testing
        lowest permitted bounds.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_integer_data_valid(-0, False))

    def test_is_integer_data_valid_cannot_be_zero_negative_infinity_numpy(cls):
        """
        Tests Trade.Trade.is_integer_data_valid().

        Trade.is_integer_data_valid() is passed negative infinity
        instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_integer_data_valid(np.NINF, False))

    def test_is_integer_data_valid_cannot_be_zero_none(cls):
        """
        Tests Trade.Trade.is_integer_data_valid().

        Trade.is_integer_data_valid() is passed None instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_integer_data_valid(None, False))

    def test_is_integer_data_valid_cannot_be_zero_not_a_number_numpy(cls):
        """
        Tests Trade.Trade.is_integer_data_valid().

        Trade.is_integer_data_valid() is passed nan(Not A Number)
        instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_integer_data_valid(np.nan, False))

    def test_is_integer_data_valid_cannot_be_zero_plus_number_minus_bigger_number(cls):
        """
        Tests Trade.Trade.is_integer_data_valid().

        Trade.is_integer_data_valid() is passed a compound argument (adding 2
        numbers together) instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_integer_data_valid(+ 1 - 2, False))

    def test_is_integer_data_valid_can_be_zero_float(cls):
        """
        Tests Trade.Trade.is_integer_data_valid().

        Trade.is_integer_data_valid() is passed a float instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_integer_data_valid(3.4, True))

    def test_is_integer_data_valid_can_be_zero_infinity_numpy(cls):
        """
        Tests Trade.Trade.is_integer_data_valid().

        Trade.is_integer_data_valid() is passed infinity instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_integer_data_valid(np.inf, True))

    def test_is_integer_data_valid_can_be_zero_less_than_zero(cls):
        """
        Tests Trade.Trade.is_integer_data_valid().

        Trade.is_integer_data_valid() is passed an int less than zero.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_integer_data_valid(-1, True))

    def test_is_integer_data_valid_can_be_zero_minus_zero(cls):
        """
        Tests Trade.Trade.is_integer_data_valid().

        Trade.is_integer_data_valid() is passed an int (= minus zero) testing
        lowest permitted bounds.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(True, cls.Trade.is_integer_data_valid(-0, True))

    def test_is_integer_data_valid_can_be_zero_negative_infinity_numpy(cls):
        """
        Tests Trade.Trade.is_integer_data_valid().

        Trade.is_integer_data_valid() is passed negative infinity
        instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_integer_data_valid(np.NINF, True))

    def test_is_integer_data_valid_can_be_zero_none(cls):
        """
        Tests Trade.Trade.is_integer_data_valid().

        Trade.is_integer_data_valid() is passed None instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_integer_data_valid(None, True))

    def test_is_integer_data_valid_can_be_zero_not_a_number_numpy(cls):
        """
        Tests Trade.Trade.is_integer_data_valid().

        Trade.is_integer_data_valid() is passed nan(Not A Number)
        instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_integer_data_valid(np.nan, True))

    def test_is_integer_data_valid_can_be_zero_plus_number_minus_bigger_number(cls):
        """
        Tests Trade.Trade.is_integer_data_valid().

        Trade.is_integer_data_valid() is passed a compound argument (adding 2
        numbers together) instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_integer_data_valid(+ 1 - 2, True))

    def test_is_method_name_valid_boolean(cls):
        """
        Tests Trade.Trade.is_method_name_valid().

        Trade.is_method_name_valid() passed int instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_method_name_valid(False))

    def test_is_method_name_valid_integer(cls):
        """
        Tests Trade.Trade.is_method_name_valid().

        Trade.is_method_name_valid() passed int instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_method_name_valid(666))

    def test_is_method_name_valid_float(cls):
        """
        Tests Trade.Trade.is_method_name_valid().

        Trade.is_method_name_valid() passed float instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_method_name_valid(66.6))

    def test_is_method_name_valid_none(cls):
        """
        Tests Trade.Trade.is_method_name_valid().

        Trade.is_method_name_valid() passed None instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_method_name_valid(None))

    def test_is_method_name_valid_nothing(cls):
        """
        Tests Trade.Trade.is_method_name_valid().

        Trade.is_method_name_valid() passed nothing instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False
                        , cls.Trade.is_method_name_valid(""))

    def test_is_method_name_valid_not_alphanumeric(cls):
        """
        Tests Trade.Trade.is_method_name_valid().

        Trade.is_method_name_valid() passed a non-alphanumeric string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_method_name_valid("12.3"))

    def test_is_method_name_valid_not_alphanumeric_2(cls):
        """
        Tests Trade.Trade.is_method_name_valid().

        Trade.is_method_name_valid() passed a non-alphanumeric string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_method_name_valid("ab/3"))

    def test_is_method_name_valid_not_alphanumeric_3(cls):
        """
        Tests Trade.Trade.is_method_name_valid().

        Trade.is_method_name_valid() passed a non-alphanumeric string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_method_name_valid("a/+*-b."))

    def test_is_method_name_valid_not_alphanumeric_4(cls):
        """
        Tests Trade.Trade.is_method_name_valid().

        Trade.is_method_name_valid() passed a non-alphanumeric string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_method_name_valid("ab?$"))

    def test_is_method_name_valid_not_a_number(cls):
        """
        Tests Trade.Trade.is_method_name_valid().

        Trade.is_method_name_valid() passed not a number instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_method_name_valid(np.nan))

    def test_is_method_name_valid_too_short(cls):
        """
        Tests Trade.Trade.is_method_name_valid().

        Trade.is_method_name_valid() passed a too short string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_method_name_valid("___"))

    def test_is_originating_name_valid_boolean(cls):
        """
        Tests Trade.Trade.is_originating_name_valid().

        Trade.is_originating_name_valid() passed int instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_originating_name_valid(False))

    def test_is_originating_name_valid_integer(cls):
        """
        Tests Trade.Trade.is_originating_name_valid().

        Trade.is_originating_name_valid() passed int instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_originating_name_valid(666))

    def test_is_originating_name_valid_float(cls):
        """
        Tests Trade.Trade.is_originating_name_valid().

        Trade.is_originating_name_valid() passed float instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_originating_name_valid(66.6))

    def test_is_originating_name_valid_none(cls):
        """
        Tests Trade.Trade.is_originating_name_valid().

        Trade.is_originating_name_valid() passed None instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_originating_name_valid(None))

    def test_is_originating_name_valid_nothing(cls):
        """
        Tests Trade.Trade.is_originating_name_valid().

        Trade.is_originating_name_valid() passed nothing instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False
                        , cls.Trade.is_originating_name_valid(""))

    def test_is_originating_name_valid_not_alphanumeric(cls):
        """
        Tests Trade.Trade.is_originating_name_valid().

        Trade.is_originating_name_valid() passed a non-alphanumeric string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_originating_name_valid("12.3"))

    def test_is_originating_name_valid_not_alphanumeric_2(cls):
        """
        Tests Trade.Trade.is_originating_name_valid().

        Trade.is_originating_name_valid() passed a non-alphanumeric string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_originating_name_valid("ab/3"))

    def test_is_originating_name_valid_not_alphanumeric_3(cls):
        """
        Tests Trade.Trade.is_originating_name_valid().

        Trade.is_originating_name_valid() passed a non-alphanumeric string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_originating_name_valid("a/+*-b."))

    def test_is_originating_name_valid_not_alphanumeric_4(cls):
        """
        Tests Trade.Trade.is_originating_name_valid().

        Trade.is_originating_name_valid() passed a non-alphanumeric string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_originating_name_valid("ab?$"))

    def test_is_originating_name_valid_not_a_number(cls):
        """
        Tests Trade.Trade.is_originating_name_valid().

        Trade.is_originating_name_valid() passed not a number instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_originating_name_valid(np.nan))

    def test_is_originating_name_valid_too_short(cls):
        """
        Tests Trade.Trade.is_originating_name_valid().

        Trade.is_originating_name_valid() passed a too short string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_originating_name_valid("___"))

    def test_is_price_per_unit_data_valid_float(cls):
        """
        Tests Trade.Trade.is_price_per_unit_data_valid().

        Trade.is_price_per_unit_data_valid() is passed a float instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.
        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_price_per_unit_data_valid(3.4))

    def test_is_price_per_unit_data_valid_infinity_numpy(cls):
        """
        Tests Trade.Trade.is_price_per_unit_data_valid().

        Trade.is_price_per_unit_data_valid() is passed infinity instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.
        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_price_per_unit_data_valid(np.inf))

    def test_is_price_per_unit_data_valid_less_than_zero(cls):
        """
        Tests Trade.Trade.is_price_per_unit_data_valid().

        Trade.is_price_per_unit_data_valid() is passed a Decimal less than zero.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables
        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_price_per_unit_data_valid(-1))

    def test_is_price_per_unit_data_valid_minus_zero(cls):
        """
        Tests Trade.Trade.is_price_per_unit_data_valid().

        Trade.is_price_per_unit_data_valid() is passed a Decimal (= minus zero) testing
        lowest permitted bounds.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables
        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_price_per_unit_data_valid(-0))

    def test_is_price_per_unit_data_valid_negative_infinity_numpy(cls):
        """
        Tests Trade.Trade.is_price_per_unit_data_valid().

        Trade.is_price_per_unit_data_valid() is passed negative infinity
        instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.
        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_price_per_unit_data_valid(np.NINF))

    def test_is_price_per_unit_data_valid_none(cls):
        """
        Tests Trade.Trade.is_price_per_unit_data_valid().

        Trade.is_price_per_unit_data_valid() is passed None instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.
        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_price_per_unit_data_valid(None))

    def test_is_price_per_unit_data_valid_not_a_number_numpy(cls):
        """
        Tests Trade.Trade.is_price_per_unit_data_valid().

        Trade.is_price_per_unit_data_valid() is passed nan(Not A Number)
        instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.
        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_price_per_unit_data_valid(np.nan))

    def test_is_price_per_unit_data_valid_plus_number_minus_bigger_number(cls):
        """
        Tests Trade.Trade.is_price_per_unit_data_valid().

        Trade.is_price_per_unit_data_valid() is passed a compound argument (adding 2
        numbers together) instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.
        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False, cls.Trade.is_price_per_unit_data_valid(+ 1 - 2))

    def test_is_settlement_date_data_valid_integer(cls):
        """
        Tests Trade.Trade.is_settlement_date_data_valid().

        Trade.is_settlement_date_data_valid() passed int instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_settlement_date_data_valid(666))

    def test_is_settlement_date_data_valid_float(cls):
        """
        Tests Trade.Trade.is_settlement_date_data_valid().

        Trade.is_settlement_date_data_valid() passed float instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_settlement_date_data_valid(66.6))

    def test_is_settlement_date_data_valid_none(cls):
        """
        Tests Trade.Trade.is_settlement_date_data_valid().

        Trade.is_settlement_date_data_valid() passed None instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_settlement_date_data_valid(None))

    def test_is_settlement_date_data_valid_nothing(cls):
        """
        Tests Trade.Trade.is_settlement_date_data_valid().

        Trade.is_settlement_date_data_valid() passed nothing instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False
                        , cls.Trade.is_settlement_date_data_valid(""))

    def test_is_settlement_date_data_valid_alphabetic(cls):
        """
        Tests Trade.Trade.is_settlement_date_data_valid().

        Trade.is_settlement_date_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_settlement_date_data_valid("123"))

    def test_is_settlement_date_data_valid_not_a_number(cls):
        """
        Tests Trade.Trade.is_settlement_date_data_valid().

        Trade.is_settlement_date_data_valid() passed not a number instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_settlement_date_data_valid(np.nan))

    def test_is_settlement_date_data_valid_too_early(cls):
        """
        Tests Trade.Trade.is_settlement_date_data_valid().

        Trade.is_settlement_date_data_valid() passed not a number instead of a datetime.datetime.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_settlement_date_data_valid(Trade.TRADE_DATE_EARLIEST - timedelta(days=1)))

    def test_is_trade_decimal_data_valid_cannot_be_zero_float(cls):
        """
        Tests Trade.Trade.is_trade_decimal_data_valid().

        Trade.is_trade_decimal_data_valid() is passed a float instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_trade_decimal_data_valid(3.4
                                                                     , Trade.IS_AGREED_FX_DATA_VALID,
                                                                     Trade.AGREED_FX_DECIMAL, False))

    def test_is_trade_decimal_data_valid_cannot_be_zero_infinity_numpy(cls):
        """
        Tests Trade.Trade.is_trade_decimal_data_valid().

        Trade.is_trade_decimal_data_valid() is passed infinity instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_trade_decimal_data_valid(np.inf
                                                                     , Trade.IS_AGREED_FX_DATA_VALID,
                                                                     Trade.AGREED_FX_DECIMAL, False))

    def test_is_trade_decimal_data_valid_cannot_be_zero_less_than_zero(cls):
        """
        Tests Trade.Trade.is_trade_decimal_data_valid().

        Trade.is_trade_decimal_data_valid() is passed a Decimal less than zero.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_trade_decimal_data_valid(-1
                                                                     , Trade.IS_AGREED_FX_DATA_VALID,
                                                                     Trade.AGREED_FX_DECIMAL, False))

    def test_is_trade_decimal_data_valid_cannot_be_zero_minus_zero(cls):
        """
        Tests Trade.Trade.is_trade_decimal_data_valid().

        Trade.is_trade_decimal_data_valid() is passed a Decimal (= minus zero) testing
        lowest permitted bounds.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_trade_decimal_data_valid(-0
                                                                     , Trade.IS_AGREED_FX_DATA_VALID,
                                                                     Trade.AGREED_FX_DECIMAL, False))

    def test_is_trade_decimal_data_valid_cannot_be_zero_negative_infinity_numpy(cls):
        """
        Tests Trade.Trade.is_trade_decimal_data_valid().

        Trade.is_trade_decimal_data_valid() is passed negative infinity
        instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_trade_decimal_data_valid(np.NINF
                                                                     , Trade.IS_AGREED_FX_DATA_VALID,
                                                                     Trade.AGREED_FX_DECIMAL, False))

    def test_is_trade_decimal_data_valid_cannot_be_zero_none(cls):
        """
        Tests Trade.Trade.is_trade_decimal_data_valid().

        Trade.is_trade_decimal_data_valid() is passed None instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_trade_decimal_data_valid(None
                                                                     , Trade.IS_AGREED_FX_DATA_VALID,
                                                                     Trade.AGREED_FX_DECIMAL, False))

    def test_is_trade_decimal_data_valid_cannot_be_zero_not_a_number_numpy(cls):
        """
        Tests Trade.Trade.is_trade_decimal_data_valid().

        Trade.is_trade_decimal_data_valid() is passed nan(Not A Number)
        instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_trade_decimal_data_valid(np.nan
                                                                     , Trade.IS_AGREED_FX_DATA_VALID,
                                                                     Trade.AGREED_FX_DECIMAL, False))

    def test_is_trade_decimal_data_valid_cannot_be_zero_plus_number_minus_bigger_number(cls):
        """
        Tests Trade.Trade.is_trade_decimal_data_valid().

        Trade.is_trade_decimal_data_valid() is passed a compound argument (adding 2
        numbers together) instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_trade_decimal_data_valid(+ 1 - 2
                                                                     , Trade.IS_AGREED_FX_DATA_VALID,
                                                                     Trade.AGREED_FX_DECIMAL, False))

    def test_is_trade_decimal_data_valid_can_be_zero_float(cls):
        """
        Tests Trade.Trade.is_trade_decimal_data_valid().

        Trade.is_trade_decimal_data_valid() is passed a float instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_trade_decimal_data_valid(3.4, Trade.IS_AGREED_FX_DATA_VALID,
                                                                     Trade.AGREED_FX_DECIMAL, True))

    def test_is_trade_decimal_data_valid_can_be_zero_infinity_numpy(cls):
        """
        Tests Trade.Trade.is_trade_decimal_data_valid().

        Trade.is_trade_decimal_data_valid() is passed infinity instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_trade_decimal_data_valid(np.inf
                                                                     , Trade.IS_AGREED_FX_DATA_VALID,
                                                                     Trade.AGREED_FX_DECIMAL, True))

    def test_is_trade_decimal_data_valid_can_be_zero_less_than_zero(cls):
        """
        Tests Trade.Trade.is_trade_decimal_data_valid().

        Trade.is_trade_decimal_data_valid() is passed a Decimal less than zero.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_trade_decimal_data_valid(-1
                                                                     , Trade.IS_AGREED_FX_DATA_VALID,
                                                                     Trade.AGREED_FX_DECIMAL, True))

    def test_is_trade_decimal_data_valid_can_be_zero_minus_zero(cls):
        """
        Tests Trade.Trade.is_trade_decimal_data_valid().

        Trade.is_trade_decimal_data_valid() is passed a Decimal (= minus zero) testing
        lowest permitted bounds.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_trade_decimal_data_valid(-0
                                                                     , Trade.IS_AGREED_FX_DATA_VALID,
                                                                     Trade.AGREED_FX_DECIMAL, True))

    def test_is_trade_decimal_data_valid_can_be_zero_negative_infinity_numpy(cls):
        """
        Tests Trade.Trade.is_trade_decimal_data_valid().

        Trade.is_trade_decimal_data_valid() is passed negative infinity
        instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_trade_decimal_data_valid(np.NINF
                                                                     , Trade.IS_AGREED_FX_DATA_VALID,
                                                                     Trade.AGREED_FX_DECIMAL, True))

    def test_is_trade_decimal_data_valid_can_be_zero_none(cls):
        """
        Tests Trade.Trade.is_trade_decimal_data_valid().

        Trade.is_trade_decimal_data_valid() is passed None instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_trade_decimal_data_valid(None
                                                                     , Trade.IS_AGREED_FX_DATA_VALID,
                                                                     Trade.AGREED_FX_DECIMAL, True))

    def test_is_trade_decimal_data_valid_can_be_zero_not_a_number_numpy(cls):
        """
        Tests Trade.Trade.is_trade_decimal_data_valid().

        Trade.is_trade_decimal_data_valid() is passed nan(Not A Number)
        instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_trade_decimal_data_valid(np.nan
                                                                     , Trade.IS_AGREED_FX_DATA_VALID,
                                                                     Trade.AGREED_FX_DECIMAL, True))

    def test_is_trade_decimal_data_valid_can_be_zero_plus_number_minus_bigger_number(cls):
        """
        Tests Trade.Trade.is_trade_decimal_data_valid().

        Trade.is_trade_decimal_data_valid() is passed a compound argument (adding 2
        numbers together) instead of a decimal.Decimal.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_trade_decimal_data_valid(+ 1 - 2
                                                                     , Trade.IS_AGREED_FX_DATA_VALID,
                                                                     Trade.AGREED_FX_DECIMAL, True))

    def test_is_trade_string_data_valid_integer(cls):
        """
        Tests Trade.Trade.is_trade_string_data_valid().

        Trade.is_trade_string_data_valid() passed int instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_trade_string_data_valid(666
                                                               , Trade.IS_CURRENCY_DATA_VALID, Trade.CURRENCY_STRING
                                                               , cls.Trade.get_currency_length()))

    def test_is_trade_string_data_valid_float(cls):
        """
        Tests Trade.Trade.is_trade_string_data_valid().

        Trade.is_trade_string_data_valid() passed float instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_trade_string_data_valid(66.6
                                                               , Trade.IS_CURRENCY_DATA_VALID, Trade.CURRENCY_STRING
                                                               , cls.Trade.get_currency_length()))

    def test_is_trade_string_data_valid_none(cls):
        """
        Tests Trade.Trade.is_trade_string_data_valid().

        Trade.is_trade_string_data_valid() passed None instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_trade_string_data_valid(None
                                                               , Trade.IS_CURRENCY_DATA_VALID, Trade.CURRENCY_STRING
                                                               , cls.Trade.get_currency_length()))

    def test_is_trade_string_data_valid_nothing(cls):
        """
        Tests Trade.Trade.is_trade_string_data_valid().

        Trade.is_trade_string_data_valid() passed nothing instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False
                        , cls.Trade.is_trade_string_data_valid(""
                                                               , Trade.IS_CURRENCY_DATA_VALID, Trade.CURRENCY_STRING
                                                               , cls.Trade.get_currency_length))

    def test_is_trade_string_data_valid_not_alphabetic(cls):
        """
        Tests Trade.Trade.is_trade_string_data_valid().

        Trade.is_trade_string_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_trade_string_data_valid("123"
                                                               , Trade.IS_CURRENCY_DATA_VALID, Trade.CURRENCY_STRING,
                                                               cls.Trade.get_currency_length()))

    def test_is_trade_string_data_valid_not_alphabetic_2(cls):
        """
        Tests Trade.Trade.is_trade_string_data_valid().

        Trade.is_trade_string_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_trade_string_data_valid("ab3"
                                                               , Trade.IS_CURRENCY_DATA_VALID, Trade.CURRENCY_STRING,
                                                               cls.Trade.get_currency_length()))

    def test_is_trade_string_data_valid_not_alphabetic_3(cls):
        """
        Tests Trade.Trade.is_trade_string_data_valid().

        Trade.is_trade_string_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_trade_string_data_valid("ab."
                                                               , Trade.IS_CURRENCY_DATA_VALID, Trade.CURRENCY_STRING,
                                                               cls.Trade.get_currency_length()))

    def test_is_trade_string_data_valid_not_alphabetic_4(cls):
        """
        Tests Trade.Trade.is_trade_string_data_valid().

        Trade.is_trade_string_data_valid() passed a non-alphabetic string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_trade_string_data_valid("ab$"
                                                               , Trade.IS_CURRENCY_DATA_VALID, Trade.CURRENCY_STRING,
                                                               cls.Trade.get_currency_length()))

    def test_is_trade_string_data_valid_not_a_number(cls):
        """
        Tests Trade.Trade.is_trade_string_data_valid().

        Trade.is_trade_string_data_valid() passed not a number instead of a string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_trade_string_data_valid(np.nan
                                                               , Trade.IS_CURRENCY_DATA_VALID, Trade.CURRENCY_STRING,
                                                               cls.Trade.get_currency_length()))

    def test_is_trade_string_data_valid_too_long(cls):
        """
        Tests Trade.Trade.is_trade_string_data_valid().

        Trade.is_trade_string_data_valid() passed a too long string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_trade_string_data_valid("abcd"
                                                               , Trade.IS_CURRENCY_DATA_VALID, Trade.CURRENCY_STRING,
                                                               cls.Trade.get_currency_length()))

    def test_is_trade_string_data_valid_too_short(cls):
        """
        Tests Trade.Trade.is_trade_string_data_valid().

        Trade.is_trade_string_data_valid() passed a too short string.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """
        cls.assertEqual(False
                        , cls.Trade.is_trade_string_data_valid("12"
                                                               , Trade.IS_CURRENCY_DATA_VALID, Trade.CURRENCY_STRING,
                                                               cls.Trade.get_currency_length()))

    def test_is_units_data_valid_float(cls):
        """
        Tests Trade.Trade.is_units_data_valid().

        Trade.is_units_data_valid() is passed a float instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_units_data_valid(3.4))

    def test_is_units_data_valid_infinity_numpy(cls):
        """
        Tests Trade.Trade.is_units_data_valid().

        Trade.is_units_data_valid() is passed infinity instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_units_data_valid(np.inf))

    def test_is_units_data_valid_less_than_zero(cls):
        """
        Tests Trade.Trade.is_units_data_valid().

        Trade.is_units_data_valid() is passed an int less than zero.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_units_data_valid(-1))

    def test_is_units_data_valid_minus_zero(cls):
        """
        Tests Trade.Trade.is_units_data_valid().

        Trade.is_units_data_valid() is passed an int (= minus zero) testing
        lowest permitted bounds.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(True, cls.Trade.is_units_data_valid(-0))

    def test_is_units_data_valid_negative_infinity_numpy(cls):
        """
        Tests Trade.Trade.is_units_data_valid().

        Trade.is_units_data_valid() is passed negative infinity
        instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_units_data_valid(np.NINF))

    def test_is_units_data_valid_none(cls):
        """
        Tests Trade.Trade.is_units_data_valid().

        Trade.is_units_data_valid() is passed None instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_units_data_valid(None))

    def test_is_units_data_valid_not_a_number_numpy(cls):
        """
        Tests Trade.Trade.is_units_data_valid().

        Trade.is_units_data_valid() is passed nan(Not A Number)
        instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_units_data_valid(np.nan))

    def test_is_units_data_valid_plus_number_minus_bigger_number(cls):
        """
        Tests Trade.Trade.is_units_data_valid().

        Trade.is_units_data_valid() is passed a compound argument (adding 2
        numbers together) instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_units_data_valid(+ 1 - 2))

    def test_is_variable_length_valid_boolean(cls):
        """
        Tests Trade.Trade.is_variable_length_valid().

        Trade.is_variable_length_valid() is passed a float instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_variable_length_valid(False))

    def test_is_variable_length_valid_float(cls):
        """
        Tests Trade.Trade.is_variable_length_valid().

        Trade.is_variable_length_valid() is passed a float instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_variable_length_valid(3.4))

    def test_is_variable_length_valid_infinity_numpy(cls):
        """
        Tests Trade.Trade.is_variable_length_valid().

        Trade.is_variable_length_valid() is passed infinity instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_variable_length_valid(np.inf))

    def test_is_variable_length_valid_less_than_zero(cls):
        """
        Tests Trade.Trade.is_variable_length_valid().

        Trade.is_variable_length_valid() is passed an int less than zero.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_variable_length_valid(-1))

    def test_is_variable_length_valid_minus_zero(cls):
        """
        Tests Trade.Trade.is_variable_length_valid().

        Trade.is_variable_length_valid() is passed an int (= minus zero) testing
        lowest permitted bounds.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_variable_length_valid(-0))

    def test_is_variable_length_valid_negative_infinity_numpy(cls):
        """
        Tests Trade.Trade.is_variable_length_valid().

        Trade.is_variable_length_valid() is passed negative infinity
        instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_variable_length_valid(np.NINF))

    def test_is_variable_length_valid_none(cls):
        """
        Tests Trade.Trade.is_variable_length_valid().

        Trade.is_variable_length_valid() is passed None instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_variable_length_valid(None))

    def test_is_variable_length_valid_not_a_number_numpy(cls):
        """
        Tests Trade.Trade.is_variable_length_valid().

        Trade.is_variable_length_valid() is passed nan(Not A Number)
        instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_variable_length_valid(np.nan))

    def test_is_variable_length_valid_plus_number_minus_bigger_number(cls):
        """
        Tests Trade.Trade.is_variable_length_valid().

        Trade.is_variable_length_valid() is passed a compound argument (adding 2
        numbers together) instead of an int.

        Parameters
        ----------
        cls : class
            Class reference accessing class functions and class variables.

        Returns
        -------
        bool
            True / False
        """

        cls.assertEqual(False, cls.Trade.is_variable_length_valid(+ 1 - 2))

    if __name__ == '__main__':
        unittest.main()