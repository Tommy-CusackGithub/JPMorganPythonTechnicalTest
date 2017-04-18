#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Mar - Apr 2017

@author: Tommy Cusack
"""
import datetime as datetime
import logging
import numpy as np

from datetime import timedelta

# import Utility as Utility

DAY_OF_WORK_PERIOD_MINIMUM = 0
DAY_OF_WORK_PERIOD_MAXIMUM = 6
INDEX_WORK_PERIOD_START = 0
INDEX_WORK_PERIOD_STOP = 1
WORK_PERIOD_DAYS = 7

CURRENCIES = ["AED", "SAR", "SGP"]
SETTLEMENT_DATE_DEFAULT = None
WORK_PERIODS = {"AED": [6, 3], "SAR": [6, 3], "SGP": [0, 4]}
WORK_PERIOD_DEFAULT = []


class WorkPeriod(object):
    # TODO: Add add/remove currencies
    logger = logging.getLogger(__name__)

    @classmethod
    def calculate_settlement_date(cls, currency: str, settlement_date_date: datetime.date):
        settlement_date_calculated = cls.get_settlement_date_default()

        try:
            time_delta_days = None
            work_period = cls.get_work_period_default()

            if cls.is_currency_valid(currency):
                work_period = cls.get_work_period(currency)
                weekday = settlement_date_date.weekday()

                if (weekday == 5 or weekday == 6
                    or weekday == work_period[INDEX_WORK_PERIOD_STOP]):
                    time_delta_days = timedelta(days=+ (WORK_PERIOD_DAYS - weekday))
                else:
                    time_delta_days = timedelta(days=+1)

                settlement_date_calculated = settlement_date_date + time_delta_days
            else:
                settlement_date_calculated = cls.get_settlement_date_default()
        except Exception as exception:
            settlement_date_calculated = cls.get_settlement_date_default()
            cls.logger.warning('Exception occurred when attempting to calculate settlement date.', exc_info=True)

        return settlement_date_calculated

    @classmethod
    def get_currencies(cls):
        return CURRENCIES

    @classmethod
    def get_currencies_count(cls):
        currencies_count = 0

        try:
            currencies_count = len(CURRENCIES)
        except Exception as exception:
            currencies_count = 0
            cls.logger.warning('Exception occurred when attempting to determine currency count.', exc_info=True)

        return currencies_count

    @classmethod
    def generate_random_currency(cls):
        random_currency = CURRENCIES[0]

        try:
            random_index = np.random.randint(low=0, high=cls.get_currencies_count())

            random_currency = CURRENCIES[random_index]
        except Exception as exception:
            random_currency = CURRENCIES[0]
            cls.logger.warning('Exception occurred when attempting random currency generation.', exc_info=True)

        return random_currency

    @classmethod
    def get_settlement_date_default(cls):
        return SETTLEMENT_DATE_DEFAULT

    @classmethod
    def get_work_periods(cls):
        return WORK_PERIODS

    @classmethod
    def get_work_period(cls, currency: str):
        work_period = WORK_PERIOD_DEFAULT

        try:
            cls.logger.info("cls.is_currency_valid(currency) = %s", cls.is_currency_valid(currency))
            if cls.is_currency_valid(currency):
                work_period = WORK_PERIODS[currency]
            else:
                work_period = WORK_PERIOD_DEFAULT

        except Exception as exception:
            work_period = WORK_PERIOD_DEFAULT
            cls.logger.warning('Exception occurred when retrieving work period.', exc_info=True)

        cls.logger.info("work_period = %s", work_period)
        return work_period

    @classmethod
    def get_work_period_default(cls):
        return WORK_PERIOD_DEFAULT

    @classmethod
    def get_work_period_in_days(cls):
        return WORK_PERIOD_DAYS

    @classmethod
    def is_currency_valid(cls, currency: str):
        currency_valid = False

        try:
            # currency_valid = (CURRENCIES.__contains__(currency) and currency in WORK_PERIODS.keys())
            if (currency is not None):
                if (type(currency) == str):
                    currency_valid = (CURRENCIES.__contains__(currency) and currency in WORK_PERIODS.keys())
                else:
                    currency_valid = False
                    cls.logger.info("currency can only be of type str")
            else:
                currency_valid = False
                cls.logger.info("currency cannot be None")
        except Exception as exception:
            currency_valid = False
            cls.logger.warning('Exception occurred when determining currency validity.', exc_info=True)

        return currency_valid

    @classmethod
    def is_day_of_work_period_valid(cls, day_of_work: int):
        day_of_work_period_valid = False

        try:
            if day_of_work is not None:
                if isinstance(day_of_work, (int, np.integer)):
                    if (day_of_work >= DAY_OF_WORK_PERIOD_MINIMUM
                        and day_of_work <= DAY_OF_WORK_PERIOD_MAXIMUM):
                        day_of_work_period_valid = True
                    else:
                        day_of_work_period_valid = False  # superfluous but explanatory
                        cls.logger.info("Expected 'day_of_work' = %s", day_of_work)
                        cls.logger.info(" to lie between %s", DAY_OF_WORK_PERIOD_MINIMUM)
                        cls.logger.info(" and %s", DAY_OF_WORK_PERIOD_MAXIMUM)
            else:
                cls.logger.info("day_of_work 'integer' variable cannot be None.")
        except Exception as exception:
            cls.logger.warning('Exception occurred when determining day_of_work_period validity.', exc_info=True)

        return day_of_work_period_valid


if __name__ == "__main__":
    # test_methods()
    print("__main__: WorkPeriod class runs OK")

    work_period = WorkPeriod()
    print("__main__: WorkPeriod instantiated")

