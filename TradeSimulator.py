#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Mar - Apr 2017

@author: Tommy Cusack

Main class from which suite of programs are to be run
"""

import datetime as datetime
import decimal as decimal
# import itertools as itertools
import logging
import pandas as pd
import sys as sys

from datetime import timedelta
from itertools import count, islice

import Trade as Trade
import TradeReport as TradeReport
import Utility as Utility
import WorkPeriod as WorkPeriod


class TradeSimulator():  # object

    # TODO: Add Unit Testing
    # TODO: Add Test Driven Development
    # TODO: Add Behaviour Driven Development
    # TODO: Add performance improvements

    def __init__(self):
        try:
            # set up and initialise logging
            self.setup_logging_defaults()
            # get reference to logger
            self.logger = logging.getLogger(__name__)
        except Exception as exception:
            print(" init(self) : Logging wasn't set up and initialised properly")
            print(" init(self) : Program terminating due to CRITICAL error")
            print("type(exception) = ", type(exception))  # the exception instance
            print("exception.args = ", exception.args)  # arguments stored in .args
            print("exception = ", exception)  # __str__ allows args to be printed directly,
            sys.exit(1)

        try:
            # Define and declare variables of program scope to be operated
            # upon by other methods.
            # These variables will be changed during program operation.

            self.trading_data_frame = pd.DataFrame(columns=Trade.Trade.get_column_headings())
            self.trade_report = None
            self.utility = Utility.Utility()

            self.logger.info("TradeSimulator: TradeSimulator instantiated")
        except Exception as exception:
            self.logger.critical(' FATAL exception occurred during initialisation', exc_info=True)
            sys.exit(1)

    def setup_logging_defaults(self):
        # set up logging to file
        logging.basicConfig(level=logging.DEBUG
                            , format='%(asctime)s %(name)-32s %(funcName)s(): %(levelname)-8s %(message)s'
                            , datefmt='%Y-%m-%d %H:%M'
                            , filename='TradingSimulationLogFile.log', filemode='w')
        # define a Handler which writes ERROR messages or higher to the sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.ERROR)
        # set a format which is simpler for console use
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        # tell the handler to use this format
        console.setFormatter(formatter)
        # add the handler to the root logger
        logging.getLogger('').addHandler(console)

        # Can log to the root logger, or any other logger. First the root...
        logging.info('Logging initialised from TradeSimulator.')

    def add_data_sample(self):
        # Declare variables of method scope to initialise Trade instances
        self.logger.info("Declare variables of method scope to initialise Trade instances")
        agreed_fx_decimal = None
        buy_sell_string = None
        currency_string = None
        entity_string = None
        instruction_date_date = None
        price_per_unit_decimal = None
        settlement_date_date = None
        units = None

        try:
            agreed_fx_decimal = decimal.Decimal('0.50')
            buy_sell_string = "B"
            currency_string = "SGP"
            entity_string = "foo"
            instruction_date_date = datetime.date(2016, 1, 1)
            price_per_unit_decimal = decimal.Decimal('100.25')
            settlement_date_date = datetime.date(2016, 1, 2)
            units = 200

            self.logger.info("Attempting to add sample data 1")
            if Trade.Trade.is_init_data_valid(agreed_fx_decimal, buy_sell_string
                    , currency_string, entity_string, instruction_date_date
                    , price_per_unit_decimal, settlement_date_date, units):

                self.trading_data_frame = pd.concat([self.trading_data_frame
                                                        , Trade.Trade.get_data_as_dataframe(agreed_fx_decimal
                                                                                            , buy_sell_string,
                                                                                            currency_string,
                                                                                            entity_string
                                                                                            , instruction_date_date,
                                                                                            price_per_unit_decimal
                                                                                            , settlement_date_date,
                                                                                            units)], ignore_index=True)

                self.logger.info("added sample data 1")
            else:
                self.logger.info("wrong initialisation data passed as Trade information ")

            agreed_fx_decimal = decimal.Decimal('0.22')
            buy_sell_string = "S"
            currency_string = "AED"
            entity_string = "bar"
            instruction_date_date = datetime.date(2016, 1, 5)
            price_per_unit_decimal = decimal.Decimal('150.5')
            settlement_date_date = datetime.date(2016, 1, 7)
            units = 450

            self.logger.info("Attempting to add sample data 2")
            if Trade.Trade.is_init_data_valid(agreed_fx_decimal, buy_sell_string
                    , currency_string, entity_string, instruction_date_date
                    , price_per_unit_decimal, settlement_date_date, units):

                self.trading_data_frame = pd.concat([self.trading_data_frame
                                                        , Trade.Trade.get_data_as_dataframe(agreed_fx_decimal
                                                                                            , buy_sell_string,
                                                                                            currency_string,
                                                                                            entity_string
                                                                                            , instruction_date_date,
                                                                                            price_per_unit_decimal
                                                                                            , settlement_date_date,
                                                                                            units)], ignore_index=True)

                self.logger.info("added sample data 2")
            else:
                self.logger.info("wrong initialisation data passed as Trade information ")

        except Exception as exception:
            self.logger.warning('Exception occurred when adding data sample', exc_info=True)

    def simulate_trading(self):
        try:
            self.logger.info("Simulate_trading function started")

            self.logger.info("Initalise variables before running simulate_trading loop")

            iteration_limit = 3 * Trade.Trade.get_buy_sell_instructions_count() * WorkPeriod.WorkPeriod.get_currencies_count()

            instruction_date_date = datetime.datetime.today()
            trading_period_timedelta = timedelta(days=+3 * WorkPeriod.WorkPeriod.get_work_period_in_days())

            self.logger.info("Simulate_trading loop started")
            for i in islice(count(0), iteration_limit):
                # print( str(i) + ": " +  str(random()) )
                self.trading_data_frame = pd.concat([self.trading_data_frame
                                                        , Trade.Trade.generate_random_trade_as_dataframe(
                        instruction_date_date, trading_period_timedelta)]
                                                    , ignore_index=True)
            self.logger.info("Simulate_trading loop ended")

            self.logger.info("Passing dataframe to TradeReport ")
            self.trade_report = TradeReport.TradeReport(self.trading_data_frame)
            self.trade_report.display_report()

            self.logger.info("Simulate_trading function ended")
        except Exception as exception:
            # Utility.Utility.log_exception(exception, " Serious exception occurred")
            self.logger.warning('Exception occurred when adding data sample', exc_info=True)


if __name__ == "__main__":
    try:
        trade_simulator = TradeSimulator()
        trade_simulator.add_data_sample()
        trade_simulator.simulate_trading()
        # df['Names'].unique()
        # profile.run('TradeSimulator().simulate_trading()')
    except Exception as exception:
        # Utility.Utility.log_exception(exception, " main() FATAL exception occurred")
        print("type(exception) = ", type(exception))  # the exception instance
        print("exception.args = ", exception.args)  # arguments stored in .args
        print("exception = ", exception)
        sys.exit(1)