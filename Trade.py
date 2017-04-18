#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Mar - Apr 2017

@author: Tommy Cusack
"""

import datetime as datetime
import decimal as decimal
# import itertools as itertools
import logging

import numpy as np
import numpy.random as np_random
import pandas as pd
# import string as string

# from datetime import timedelta
from itertools import count, islice
# from pandas import DataFrame
# from random import *

# import Utility as Utility
import WorkPeriod as WorkPeriod

# Define and declare variables of global scope
# Python doesn't allow constants but these variables shouldn't
# be changed during program operation except for initialisation

# Declare 'constants'

AGREED_FX = "AgreedFx"
AMOUNT = "Amount"
AMOUNT_DEFAULT = None

BUY_SELL = "Buy/Sell"
BUY_SELL_INSTRUCTIONS = ["B", "S"]
# BUY_SELL_INSTRUCTIONS_SET = {BUY_SELL_INSTRUCTIONS}
BUY_SELL_INSTRUCTIONS_READABLE_DICT = {"B": "Amount ($) settled incoming"
    , "S": "Amount ($) settled outgoing"}

CURRENCY_DEFAULT_STRING = "USD"
CURRENCY_STRING_LENGTH = 3
CURRENCY = "Currency"

ENTITY_STRING_LENGTH = 3
ENTITY = "Entity"

INSTRUCTION_DATE = "InstructionDate"

PRICE_PER_UNIT = "Price per unit"

SETTLEMENT_DATE = "SettlementDate"
SETTLEMENT_DATE_ACTUAL = "SettlementDateActual"
SETTLEMENT_DATE_DEFAULT = None

TRADE_DATE_EARLIEST = datetime.date(1776, 7, 4)
TRADE_DATE_LATEST = datetime.date(3017, 12, 31)

UNITS = "Units"

# 'constant' method names
IS_AGREED_FX_DATA_VALID = "is_agreed_fx_data_valid"
IS_BUY_SELL_DATA_VALID = "is_buy_sell_data_valid"
IS_CURRENCY_DATA_VALID = "is_currency_data_valid"
IS_ENTITY_DATA_VALID = "is_entity_data_valid"
IS_PRICE_PER_UNIT_DATA_VALID = "is_price_per_unit_data_valid"

# 'constant' variable used as argument names
AGREED_FX_DECIMAL = "agreed_fx_decimal"
BUY_SELL_STRING = "buy_sell_string"
CURRENCY_STRING = "currency_string"
ENTITY_STRING = "entity_string"
INSTRUCTION_DATE_DATETIME = "instruction_date_datetime"
PRICE_PER_UNIT_DECIMAL = "price_per_unit_decimal"
SETTLEMENT_DATE_DATE = "settlement_date_date"


class Trade(object):  #
    # Declare variables
    logger = logging.getLogger(__name__)

    def __init__(self, agreed_fx_decimal: decimal.Decimal, buy_sell_string: str
                 , currency_string: str, entity_string: str
                 , instruction_date_date: datetime.date
                 , price_per_unit_decimal: decimal.Decimal
                 , settlement_date_date: datetime.date, units: int):

        self.agreed_fx_decimal = agreed_fx_decimal
        self.amount = None
        self.buy_sell_string = buy_sell_string
        self.currency_string = currency_string
        self.entity_string = entity_string
        self.instruction_date_date = instruction_date_date
        self.price_per_unit_decimal = price_per_unit_decimal
        self.settlement_date_date = settlement_date_date
        self.settlement_date_actual_datetime = None
        self.units = units

    @classmethod
    def calculate_amount(cls, agreed_fx_decimal: decimal.Decimal
                         , price_per_unit_decimal: decimal.Decimal, units: int):

        amount = AMOUNT_DEFAULT
        error_message = None

        try:
            if (cls.is_agreed_fx_data_valid(agreed_fx_decimal)
                and cls.is_price_per_unit_data_valid(price_per_unit_decimal)
                and cls.is_units_data_valid(units)):
                amount = agreed_fx_decimal * price_per_unit_decimal * units
            else:
                if cls.is_agreed_fx_data_valid(agreed_fx_decimal):
                    error_message = "invalid agreed_fx_decimal passed to method. "
                if cls.is_price_per_unit_data_valid(price_per_unit_decimal):
                    if error_message != None:
                        error_message = "invalid price_per_unit_decimal passed to method. "
                    else:
                        error_message = error_message + "invalid price_per_unit_decimal passed to method. "
                if cls.is_units_data_valid(units):
                    if error_message != None:
                        error_message = "invalid units passed to method. "
                    else:
                        error_message = error_message + "invalid units passed to method. "

            if error_message != None:
                cls.logger.debug(error_message)

        except Exception as exception:
            cls.logger.warning('Exception occurred during calculate_amount', exc_info=True)

        return amount

    @classmethod
    def calculate_settlement_date(cls, currency_string: str, settlement_date_date: datetime.date):

        settlement_date_calculated = SETTLEMENT_DATE_DEFAULT
        error_message = None

        try:
            if (cls.is_currency_data_valid(currency_string)
                and cls.is_settlement_date_data_valid(settlement_date_date)):
                settlement_date_calculated = WorkPeriod.WorkPeriod.calculate_settlement_date(currency_string,
                                                                                             settlement_date_date)
            else:
                cls.logger.info("Data format validation failed. Constructing appropriate error message")
                if cls.is_currency_data_valid(currency_string):
                    error_message = "invalid currency_string"
                if cls.is_settlement_date_data_valid(settlement_date_date):
                    if error_message != None:
                        error_message = ", settlement_date_date"
                    else:
                        error_message = error_message + ", price_per_unit_decimal"

                if error_message != None:
                    cls.logger.info("calculate_amount : invalid " + error_message
                                    + " variables passed to method. ")
        except Exception as exception:
            cls.logger.warning("calculate_settlement_date failed due to exception.", exc_info=True)

        return settlement_date_calculated

    @classmethod
    def generate_random_agreed_fx(cls):
        agreed_fx_decimal = decimal.Decimal(0.5)

        try:
            cls.logger.info("Attempting random agreed fx generation")

            agreed_fx = np_random.randint(low=1, high=100)
            agreed_fx_decimal = decimal.Decimal(agreed_fx)
            agreed_fx_decimal = agreed_fx_decimal / 100

            cls.logger.info("Random agreed fx generation succeeded")
        except Exception as exception:
            agreed_fx_decimal = decimal.Decimal(0.5)
            cls.logger.warning("Random agreed fx generation failed..", exc_info=True)

        return agreed_fx_decimal

    @classmethod
    def generate_random_buy_sell(cls):
        random_buy_sell = BUY_SELL_INSTRUCTIONS[0]

        try:
            cls.logger.info("Attempting random buy sell generation")

            random_index = np_random.randint(low=0
                                             , high=cls.get_buy_sell_instructions_count())
            random_buy_sell = BUY_SELL_INSTRUCTIONS[random_index]

            cls.logger.info("Random buy sell generation succeeded")
        except Exception as exception:
            random_buy_sell = BUY_SELL_INSTRUCTIONS[0]
            cls.logger.warning("Random buy sell generation failed..", exc_info=True)

        return random_buy_sell

    @classmethod
    def generate_random_currency(cls):
        cls.logger.info("Generating random currency")
        return WorkPeriod.WorkPeriod.generate_random_currency()

    @classmethod
    def generate_random_entity(cls):
        random_entity = ""
        valid_letters = "abcdefghijklmnopqrstuvwxyz"

        try:
            cls.logger.info("Generating random entity")
            random_index = np_random.randint(low=0, high=len(valid_letters))

            for i in islice(count(0), cls.get_entity_length()):
                random_entity = random_entity + valid_letters[random_index]

            cls.logger.info("Random entity generation succeeded")
            #        for i in islice(count(0), cls.get_entity_length()):
            #            random_entity = random_entity + np_random.choice(valid_letters)

            # random_entity = ''.join((np_random.choice(valid_letters) for i in xrange( cls.get_entity_length() )))
        except Exception as exception:
            random_entity = "abc"
            cls.logger.warning("Random entity generation failed.", exc_info=True)

        return random_entity

    @classmethod
    def generate_random_price_per_unit(cls):
        random_price_per_unit_decimal = decimal.Decimal(1.0)

        try:
            cls.logger.info("Generating random price per unit")

            price_per_unit = np_random.randint(low=1, high=10000)
            random_price_per_unit_decimal = decimal.Decimal(price_per_unit)
            random_price_per_unit_decimal = random_price_per_unit_decimal / 100  # decimal.Decimal( )

            cls.logger.info("Random price per unit generation succeeded")
        except Exception as exception:
            random_price_per_unit_decimal = decimal.Decimal(0.5)
            cls.logger.warning("Random price per unit generation failed.", exc_info=True)

        return random_price_per_unit_decimal

    @classmethod
    def generate_random_instruction_settlement_dates(cls
                                                     , trading_period_timedelta: datetime.timedelta):

        random_instruction_date_date = None
        random_settlement_date_date = None

        random_size = 6

        try:
            cls.logger.info("Generating random instruction and settlement dates")

            random_instruction_date_date = datetime.date.today() + (np_random.randint(low=1,
                                                                                      high=random_size) / 7) * trading_period_timedelta

            random_settlement_date_date = random_instruction_date_date + (np_random.randint(low=1
                                                                                            ,
                                                                                            high=random_size) / 7) * trading_period_timedelta  # / ( 1 + random_size)

            cls.logger.info("type(random_instruction_date_date) = %s", type(random_instruction_date_date))
            cls.logger.info("type(random_settlement_date_date) = %s", type(random_settlement_date_date))

            cls.logger.info("Random instruction and settlement dates generation succeeded")
        except Exception as exception:
            random_instruction_date_date = TRADE_DATE_EARLIEST
            random_settlement_date_date = TRADE_DATE_LATEST
            cls.logger.warning("Random instruction and settlement dates generation failed.", exc_info=True)

        return random_instruction_date_date, random_settlement_date_date

    @classmethod
    def generate_random_trade_as_dataframe(cls
                                           , instruction_date_date: datetime.date
                                           , trading_period_timedelta: datetime.timedelta):

        random_trade_as_dataframe = None

        try:
            cls.logger.info("Generating random trade as dataframe")

            agreed_fx_decimal = cls.generate_random_agreed_fx()
            buy_sell_string = cls.generate_random_buy_sell()
            currency_string = cls.generate_random_currency()
            entity_string = cls.generate_random_entity()
            price_per_unit_decimal = cls.generate_random_price_per_unit()

            instruction_date_date_random, settlement_date_date = cls.generate_random_instruction_settlement_dates(
                trading_period_timedelta)

            units = cls.generate_random_unit()

            random_trade_as_dataframe = cls.get_data_as_dataframe(agreed_fx_decimal
                                                                  , buy_sell_string, currency_string, entity_string
                                                                  , instruction_date_date, price_per_unit_decimal
                                                                  , settlement_date_date, units)

            cls.logger.info("Random trade as dataframe generation succeeded")
        except Exception as exception:
            random_trade_as_dataframe = None
            cls.logger.warning("Random trade as dataframe generation failed.", exc_info=True)

        return random_trade_as_dataframe

    @classmethod
    def generate_random_unit(cls):
        unit = 1

        try:
            cls.logger.info("Generating random unit.")
            unit = np_random.randint(low=1, high=10000)
            cls.logger.info("Random unit generation succeeded")
        except Exception as exception:
            unit = 1
            cls.logger.warning("Random unit generation failed.", exc_info=True)

        return unit

    @classmethod
    def get_buy_sell_instructions(cls):
        return BUY_SELL_INSTRUCTIONS

    @classmethod
    def get_buy_sell_instructions_readable(cls):
        return BUY_SELL_INSTRUCTIONS_READABLE_DICT

    @classmethod
    def get_buy_sell_instructions_count(cls):
        return len(BUY_SELL_INSTRUCTIONS)

    @classmethod
    def get_column_headings(cls):
        return [AGREED_FX, AMOUNT, BUY_SELL, CURRENCY, ENTITY
            , INSTRUCTION_DATE, PRICE_PER_UNIT, SETTLEMENT_DATE
            , SETTLEMENT_DATE_ACTUAL, UNITS]

    @classmethod
    def get_column_heading_agreed_fx(cls):
        return AGREED_FX

    @classmethod
    def get_column_heading_amount(cls):
        return AMOUNT

    @classmethod
    def get_column_heading_buy_sell(cls):
        return BUY_SELL

    @classmethod
    def get_column_heading_currency(cls):
        return CURRENCY

    @classmethod
    def get_column_heading_entity(cls):
        return ENTITY

    @classmethod
    def get_column_heading_instruction_date(cls):
        return INSTRUCTION_DATE

    @classmethod
    def get_column_heading_price_per_unit(cls):
        return PRICE_PER_UNIT

    @classmethod
    def get_column_heading_settlement_date(cls):
        return SETTLEMENT_DATE

    @classmethod
    def get_column_heading_settlement_date_actual(cls):
        return SETTLEMENT_DATE_ACTUAL

    @classmethod
    def get_column_heading_units(cls):
        return UNITS

    @classmethod
    def get_currencies_count(cls):
        return WorkPeriod.WorkPeriod.get_currencies_count()

    @classmethod
    def get_currency_length(cls):
        return CURRENCY_STRING_LENGTH

    @classmethod
    def get_data(self):
        return [self.agreed_fx_decimal, self.buy_sell_string
            , self.currency_string, self.entity_string
            , self.instruction_date_datetime, self.price_per_unit_decimal
            , self.settlement_date_date
            , self.settlement_date_actual_datetime, self.units]

    @classmethod
    def get_data_as_dataframe(cls, agreed_fx_decimal: decimal.Decimal
                              , buy_sell_string: str, currency_string: str, entity_string: str
                              , instruction_date_datetime: datetime.date
                              , price_per_unit_decimal: decimal.Decimal
                              , settlement_date_date: datetime.date, units: int):

        return pd.DataFrame(data=[(agreed_fx_decimal
                                   , cls.calculate_amount(agreed_fx_decimal, price_per_unit_decimal, units)
                                   , buy_sell_string, currency_string
                                   , entity_string, instruction_date_datetime
                                   , price_per_unit_decimal
                                   , settlement_date_date
                                   , cls.calculate_settlement_date(currency_string, settlement_date_date)
                                   , units)], columns=cls.get_column_headings())

    @classmethod
    def get_entity_length(cls):
        return ENTITY_STRING_LENGTH

    @classmethod
    def is_agreed_fx_data_valid(cls, agreed_fx_decimal: decimal.Decimal):
        """
        Summary line.

        Extended description of function.

        Parameters
        ----------
        arg1 : int
            Description of arg1
        arg2 : str
            Description of arg2

        Returns
        -------
        int
            Description of return value

        """
        return cls.is_trade_decimal_data_valid(agreed_fx_decimal
                                               , IS_AGREED_FX_DATA_VALID, AGREED_FX_DECIMAL, False)

    @classmethod
    def is_argument_name_valid(cls, trade_string_name: str):
        return cls.is_originating_name_valid(trade_string_name)

    @classmethod
    def is_buy_sell_data_valid(cls, buy_sell_string: str):
        buy_sell_data_valid = False
        data_format_valid = False

        try:
            cls.logger.info("Validating buy sell data: start")
            data_format_valid = cls.is_trade_string_data_valid(buy_sell_string
                                                               , IS_BUY_SELL_DATA_VALID, BUY_SELL_STRING, 1)

            if data_format_valid:
                if buy_sell_string == "B" or buy_sell_string == "S":
                    buy_sell_data_valid = True
                else:
                    cls.logger.info(" 'buy_sell_string' variable can only be B or S.")
            else:
                cls.logger.info(" 'buy_sell_string' variable has an invalid data format.")

            cls.logger.info("Validating buy sell data: end")
        except Exception as exception:
            cls.logger.warning("Data validation failed.", exc_info=True)

        return buy_sell_data_valid

    @classmethod
    def is_currency_data_valid(cls, currency_string: str):
        return cls.is_trade_string_data_valid(currency_string
                                              , IS_CURRENCY_DATA_VALID, CURRENCY_STRING, cls.get_currency_length())

    @classmethod
    def is_date_valid(cls, trade_date: datetime.date, trade_date_name: str):
        data_format_valid = False
        trade_date_name_valid = False

        try:
            cls.logger.info("Validating date: start")

            trade_date_name_valid = cls.is_argument_name_valid(trade_date_name)
            if trade_date_name_valid:
                if trade_date is not None:
                    if isinstance(trade_date, datetime.date):
                        if trade_date >= TRADE_DATE_EARLIEST:
                            data_format_valid = True
                        else:
                            cls.logger.info("is_date_valid: 'trade_date' must be >= %s"
                                  , TRADE_DATE_EARLIEST)
                    else:
                        cls.logger.info(" 'trade_date' should only be of type datetime.date.")
                        cls.logger.info("type('trade_date') = %s", type(trade_date))
                else:
                    cls.logger.info("'trade_date' variable cannot be None.")
            else:
                if (~trade_date_name_valid):
                    cls.logger.info("Debugging variable '%s' is itself invalid!", trade_date_name)

            cls.logger.info("Validating date: end")
        except Exception as exception:
            cls.logger.warning("Data validation failed.", exc_info=True)

        return data_format_valid

    @classmethod
    def is_entity_data_valid(cls, entity_string: str):
        entity_data_valid = False

        try:
            entity_data_valid = cls.is_trade_string_data_valid(entity_string
                                                               , IS_ENTITY_DATA_VALID, ENTITY_STRING,
                                                               cls.get_entity_length())
        except Exception as exception:
            entity_data_valid = False
            cls.logger.warning("Init data validation failed.", exc_info=True)

        return entity_data_valid

    @classmethod
    def is_init_data_valid(cls, agreed_fx_decimal: decimal.Decimal
                           , buy_sell_string: str, currency_string: str, entity_string: str
                           , instruction_date_date: datetime.date
                           , price_per_unit_decimal: decimal.Decimal
                           , settlement_date_date: datetime.date, units: int):

        init_data_valid = False

        try:
            init_data_valid = (cls.is_agreed_fx_data_valid(agreed_fx_decimal)
                               and cls.is_buy_sell_data_valid(buy_sell_string)
                               and cls.is_currency_data_valid(currency_string)
                               and cls.is_entity_data_valid(entity_string)
                               and cls.is_instruction_and_settlement_dates_data_valid(instruction_date_date,
                                                                                      settlement_date_date)
                               and cls.is_price_per_unit_data_valid(price_per_unit_decimal)
                               and cls.is_units_data_valid(units))
        except Exception as exception:
            init_data_valid = False
            cls.logger.warning("Init data validation failed.", exc_info=True)

        return init_data_valid

    @classmethod
    def is_instruction_and_settlement_dates_data_valid(cls, instruction_date_date: datetime.date
                                                       , settlement_date_date: datetime.date):
        data_format_valid = False

        try:
            if (cls.is_date_valid(instruction_date_date, INSTRUCTION_DATE_DATETIME)
                and cls.is_date_valid(settlement_date_date, SETTLEMENT_DATE_DATE)):

                data_format_valid = (settlement_date_date >= instruction_date_date)

            else:
                data_format_valid = False
        except Exception as exception:
            data_format_valid = False
            cls.logger.warning("Data format validation failed.", exc_info=True)

        return data_format_valid

    @classmethod
    def is_instruction_date_data_valid(cls, instruction_date_datetime: datetime.date):

        return cls.is_date_valid(instruction_date_datetime, INSTRUCTION_DATE_DATETIME)

    @classmethod
    def is_integer_data_valid(cls, integer: int, can_equal_zero: bool):
        data_format_valid = False

        try:
            if integer is not None:
                if isinstance(integer, (int, np.integer)):
                    if can_equal_zero:
                        if integer >= 0:
                            data_format_valid = True
                        else:
                            cls.logger.info("Expected 'integer' variable to be >= 0.")
                    else:
                        if integer > 0:
                            data_format_valid = True
                        else:
                            cls.logger.info("Expected 'integer' variable to be > 0.")
                else:
                    cls.logger.info("'integer' variable should only be of types (int or np.integer).""")
            else:
                cls.logger.info("'integer' variable cannot be None.")
        except Exception as exception:
            cls.logger.warning("Data format validation failed.", exc_info=True)

        return data_format_valid

    @classmethod
    def is_method_name_valid(cls, method_name: str):
        method_name_valid = False
        try:
            method_name_valid = cls.is_originating_name_valid(method_name)
        except Exception as exception:
            method_name_valid = False
            cls.logger.warning("Data format validation failed.", exc_info=True)

        return method_name_valid

    @classmethod
    def is_originating_name_valid(cls, originating_name: str):
        originating_name_valid = False
        originating_name_stripped = ""

        try:
            if originating_name is not None:
                if type(originating_name) is str:
                    originating_name_stripped = (originating_name.replace("_", ""))
                    # print("is_originating_name_valid: 'originating_name_stripped' = ", originating_name_stripped)

                    if len(originating_name_stripped) > 0:
                        if originating_name_stripped.isalnum():
                            originating_name_valid = True
                        else:
                            cls.logger.info("is_originating_name_valid: '%s' variable should only contain alpha numeric characters.", originating_name)
                    else:
                        cls.logger.info("is_originating_name_valid: '%s' variable can only have length > 0.", originating_name)
                else:
                    cls.logger.info("is_originating_name_valid: Expected '%s' variable to be of type String.", originating_name)
            else:
                cls.logger.info("is_originating_name_valid: %s variable cannot be None.", originating_name)
        except Exception as exception:
            cls.logger.warning("Data format validation failed.", exc_info=True)

        return originating_name_valid

    @classmethod
    def is_price_per_unit_data_valid(cls, price_per_unit_decimal: decimal.Decimal):

        price_per_unit_data_valid = False

        try:
            price_per_unit_data_valid = cls.is_trade_decimal_data_valid(price_per_unit_decimal
                                                                        , IS_PRICE_PER_UNIT_DATA_VALID,
                                                                        PRICE_PER_UNIT_DECIMAL, True)
        except Exception as exception:
            price_per_unit_data_valid = False
            cls.logger.warning("Data format validation failed.", exc_info=True)

        return price_per_unit_data_valid

    @classmethod
    def is_settlement_date_data_valid(cls, settlement_date_date: datetime.date):
        settlement_date_data_valid = False

        try:
            settlement_date_data_valid = cls.is_date_valid(settlement_date_date, SETTLEMENT_DATE_DATE)
        except Exception as exception:
            settlement_date_data_valid = False
            cls.logger.warning("Data format validation failed.", exc_info=True)

        return settlement_date_data_valid

    @classmethod
    def is_trade_decimal_data_valid(cls, trade_decimal: decimal.Decimal
                                    , originating_method_name: str, trade_decimal_name: str
                                    , can_equal_zero: bool):

        data_format_valid = False
        method_name_valid = False
        trade_decimal_name_valid = False

        try:
            method_name_valid = cls.is_method_name_valid(originating_method_name)
            trade_decimal_name_valid = cls.is_argument_name_valid(trade_decimal_name)

            if (method_name_valid and trade_decimal_name_valid):
                if trade_decimal is not None:
                    if isinstance(trade_decimal, decimal.Decimal):  # type(trade_decimal) == decimal.Decimal:
                        if can_equal_zero:
                            if trade_decimal >= 0:
                                data_format_valid = True
                            else:
                                cls.logger.info("'%s' must be >= 0.", trade_decimal_name)
                        else:
                            if trade_decimal > 0:
                                data_format_valid = True
                            else:
                                cls.logger.info("'%s' must be > 0.", trade_decimal_name)
                    else:
                        cls.logger.info("'%s' must only be type decimal.Decimal.", trade_decimal_name)
                        cls.logger.info("type('trade_decimal') = %s", type(trade_decimal))
                else:
                    cls.logger.info("'%s' variable cannot be None.", trade_decimal_name)
            else:
                if (~method_name_valid):
                    cls.logger.info("Debugging variable '%s' is itself invalid!", originating_method_name)
                if (~trade_decimal_name_valid):
                    cls.logger.info("Debugging variable '%s' is itself invalid!", trade_decimal_name_valid)

        except Exception as exception:
            cls.logger.warning("Data format validation failed.", exc_info=True)

        return data_format_valid

    @classmethod
    def is_trade_string_data_valid(cls, trade_string: str
                                   , originating_method_name: str, trade_string_name: str
                                   , trade_string_length: int):

        data_format_valid = False
        method_name_valid = False
        trade_string_length_valid = False
        trade_string_name_valid = False

        debug_string = None
        message_string = " invoked by "
        message_string = message_string.join(originating_method_name)
        message_string = message_string.join(": Data format validation failed. ")
        message_string = message_string.join(" Cannot process data.")

        try:
            method_name_valid = cls.is_method_name_valid(originating_method_name)
            trade_string_length_valid = cls.is_variable_length_valid(trade_string_length)
            trade_string_name_valid = cls.is_argument_name_valid(trade_string_name)

            if (method_name_valid and trade_string_name_valid and trade_string_length_valid):
                if trade_string is not None:
                    if isinstance(trade_string, str):  # type(trade_string) is str:
                        if len(trade_string) == trade_string_length:
                            if trade_string.isalpha():
                                data_format_valid = True
                            else:
                                debug_string = " invoked by " + originating_method_name + ": '" + trade_string_name + "' variable should only contain alphabetic characters."
                                cls.logger.info(debug_string)
                        else:
                            cls.logger.info(" invoked by %s", originating_method_name)
                            cls.logger.info(": '%s", trade_string_name)
                            cls.logger.info("' variable can only have length = %s", trade_string_length)

                    else:
                        debug_string = " invoked by " + originating_method_name + ": Expected '" + trade_string_name + "' variable to be of type String."
                        cls.logger.info(debug_string)
                        
                else:
                    debug_string = " invoked by " + originating_method_name + ":" + trade_string_name + " variable cannot be None."
                    cls.logger.info(debug_string)
            else:
                if (~method_name_valid):
                    debug_string = " Debugging variable '" + originating_method_name + "' is itself invalid!"
                    cls.logger.info(debug_string)
                    
                if (~trade_string_length_valid):
                    cls.logger.info(" Debugging variable 'trade_string_length' = %s expected length is itself invalid!", trade_string_length )
                    
                if (~trade_string_name_valid):
                    debug_string = " Debugging variable '"+ trade_string_name + "' is itself invalid!"
                    cls.logger.info(debug_string)

        except Exception as exception:
            cls.logger.warning(message_string, exc_info=True)

        return data_format_valid

    @classmethod
    def is_units_data_valid(cls, units: int):
        units_data_valid = False

        try:
            units_data_valid = cls.is_integer_data_valid(units, True)
        except Exception as exception:
            units_data_valid = False
            cls.logger.warning("Data format validation failed.", exc_info=True)

        return units_data_valid

    @classmethod
    def is_variable_length_valid(cls, variable_length: int):
        variable_length_valid = False

        try:
            variable_length_valid = cls.is_integer_data_valid(variable_length, False)
        except Exception as exception:
            variable_length_valid = False
            cls.logger.warning("Data format validation failed.", exc_info=True)

        return variable_length_valid


if __name__ == "__main__":
    # test_methods()
    print("__main__: do Trade class runs OK")

