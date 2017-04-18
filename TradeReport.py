# -*- coding: utf-8 -*-
"""
Created Mar - Apr 2017

@author: Tommy Cusack
"""

import datetime as datetime
# import dateutil
import decimal as decimal
# import matplotlib.pyplot as plt
import itertools as itertools
import logging
import numpy as np
import numpy.random as np_random
import pandas as pd
import string as string

from datetime import timedelta
from itertools import count, islice
from pandas import DataFrame

import Trade as Trade
import Utility as Utility
import WorkPeriod as WorkPeriod


class TradeReport(object):
    def __init__(self, trading_data_frame: pd.DataFrame):
        # self.logger = logging.getLogger(__name__)

        try:
            self.logger = logging.getLogger(__name__)
            self.logger.info("initialising variables")

            self.utility = Utility.Utility()

            self.buy_sell_unique_array = None
            self.ranking_by_trade_instructions_dict = {}
            self.trade_report_settled = None

            self.logger.info("initialising variables")
            if (self.utility.is_data_frame_data_format_valid(trading_data_frame)):
                settlement_date_unique_array = trading_data_frame[
                    Trade.Trade.get_column_heading_settlement_date_actual()].unique()
                # settlement_date_unique_array_sorted =
                settlement_date_unique_array.sort(axis=0)

                self.logger.info("settlement_date_unique_array = ")
                self.logger.info(settlement_date_unique_array)
                buy_sell_unique_array = trading_data_frame[Trade.Trade.get_column_heading_buy_sell()].unique()

                columns_header = Trade.Trade.get_buy_sell_instructions() * Trade.Trade.get_buy_sell_instructions_count()
                columns_header.sort()
                self.logger.info("columns_header = %s", columns_header)

                self.trade_report_settled = pd.DataFrame(index=settlement_date_unique_array
                                                         , columns=[Trade.Trade.get_buy_sell_instructions()])

                self.logger.info("Instantiated trade_report_settled = %s", self.trade_report_settled)

                for buy_sell_unique in buy_sell_unique_array:
                    trading_ranking_data_frame = trading_data_frame[
                        (trading_data_frame[Trade.Trade.get_column_heading_buy_sell()] == buy_sell_unique)]

                    trading_ranking_selection_data_frame = trading_ranking_data_frame[
                        [Trade.Trade.get_column_heading_entity(), Trade.Trade.get_column_heading_amount()]]

                    trading_ranking_groupby_entity_data_frame = trading_ranking_selection_data_frame.groupby(
                        Trade.Trade.get_column_heading_entity())

                    trading_ranking_sum = trading_ranking_groupby_entity_data_frame.sum()
                    trading_ranking_sum_sorted = trading_ranking_sum.sort_values(
                        [Trade.Trade.get_column_heading_amount()], ascending=False)

                    self.logger.info(" trading_ranking_sum_sorted = ")
                    self.logger.info(trading_ranking_sum_sorted)
                    self.ranking_by_trade_instructions_dict[buy_sell_unique] = trading_ranking_sum_sorted

                    for settlement_date_unique in settlement_date_unique_array:
                        # print("TradeSimulator::simulate_trading(): buy_sell_unique = " + buy_sell_unique)
                        trading_selection_data_frame = trading_data_frame[
                            (trading_data_frame[
                                 Trade.Trade.get_column_heading_settlement_date_actual()] == settlement_date_unique)
                            & (trading_data_frame[Trade.Trade.get_column_heading_buy_sell()] == buy_sell_unique)]

                        trading_selection_data_frame = trading_selection_data_frame[
                            [Trade.Trade.get_column_heading_entity(), Trade.Trade.get_column_heading_amount()]]
                        # trading_selection_data_frame = trading_selection_data_frame[ trading_selection_data_frame[Trade.Trade.get_column_heading_entity()] , trading_selection_data_frame[ Trade.Trade.get_column_heading_amount] ]
                        # print("TradeSimulator::simulate_trading(): trading_selection_data_frame = ", trading_selection_data_frame)

                        trading_groupby_entity_data_frame = trading_selection_data_frame.groupby(
                            Trade.Trade.get_column_heading_entity())  # .sum() # , Trade.Trade.get_column_heading_buy_sell() .get_column_heading_settlement_date_actual
                        #                print("TradeSimulator::simulate_trading(): groupby.get_column_heading_entity()")
                        #                print(trading_groupby_entity_data_frame.head())
                        # Apply the sum function to the groupby object
                        trading_sum = pd.DataFrame(data=[trading_groupby_entity_data_frame.sum()])  #

                        trading_sum = trading_groupby_entity_data_frame.sum()
                        trading_sum_sorted = trading_sum.sort_values([Trade.Trade.get_column_heading_amount()],
                                                                     ascending=False)

                        self.logger.info("trading_sum_sorted = ")
                        self.logger.info(trading_sum_sorted)
                        # self.display_variable_from_class_method(CLASS_METHOD_NAME, trading_sum_sorted)
                        # self.utility.get_class_method_name(STACK)

                        self.trade_report_settled.ix[settlement_date_unique][buy_sell_unique] = self.calculate_sum(
                            trading_sum_sorted)
                        # trade_report_sorted.ix[settlement_date_unique][buy_sell_unique] [Trade.Trade.get_column_heading_entity()] = trading_sum_sorted[Trade.Trade.get_column_heading_entity()]


                        # trade_report_settled[settlement_date_unique] = 1 # self.calculate_sum(trading_sum_sorted)

                self.logger.info("AFTER: trade_report_settled = ")
                self.logger.info(self.trade_report_settled)

                #                for buy_sell_unique in buy_sell_unique_array:
                #                    trading_ranking_data_frame = trading_data_frame[
                #                        ( trading_data_frame[Trade.Trade.get_column_heading_buy_sell()] == buy_sell_unique ) ]
                #
                #                    trading_ranking_selection_data_frame = trading_ranking_data_frame[ [ Trade.Trade.get_column_heading_entity() , Trade.Trade.get_column_heading_amount() ] ]
                #
                #    #                print(" trading_ranking_selection_data_frame = ")
                #    #                print(trading_ranking_selection_data_frame)
                #
                #                    trading_ranking_groupby_entity_data_frame = trading_ranking_selection_data_frame.groupby(
                #                            Trade.Trade.get_column_heading_entity())
                #
                #                    trading_ranking_sum = trading_ranking_groupby_entity_data_frame.sum()
                #                    trading_ranking_sum_sorted = trading_ranking_sum.sort_values([Trade.Trade.get_column_heading_amount()], ascending=False)
                #
                #                    self.logger.info(" trading_ranking_sum_sorted = ")
                #                    self.logger.info(trading_ranking_sum_sorted)
                #                    ranking_by_trade_instructions_dict[buy_sell_unique] = trading_ranking_sum_sorted

                self.logger.info("ranking_by_trade_instructions_dict = %s", self.ranking_by_trade_instructions_dict)
                # self.logger.info(ranking_by_trade_instructions_dict)

                # sums = df['data1'].groupby([df['key1'], df['key2']]).sum()

                #            trading_groupby_data_frame = trading_data_frame[ Trade.Trade.get_column_heading_amount() ].groupby([trading_data_frame[ Trade.Trade.get_column_heading_settlement_date_actual() ]
                #                , trading_data_frame[ Trade.Trade.get_column_heading_entity() ]
                #                , trading_data_frame[ Trade.Trade.get_column_heading_buy_sell() ]
                #                ]).sum()
                #
                ##            trading_groupby_data_frame = trading_data_frame.groupby(
                ##                        Trade.Trade.get_column_heading_entity()
                ##                        , Trade.Trade.get_column_heading_settlement_date_actual())
                #            print("TradeReport::__init__: trading_groupby_data_frame = ", trading_groupby_data_frame)
                #
                ##            trading_groupby_data_frame = trading_groupby_data_frame.sort_values([Trade.Trade.get_column_heading_amount()], ascending=False)
                ##            print("TradeReport::__init__: trading_groupby_data_frame = ", trading_groupby_data_frame)
                #
                #            trading_unstack_data_frame = trading_groupby_data_frame.unstack()
                #            # trading_unstack_data_frame = trading_unstack_data_frame.unstack()
                #            print("TradeReport::__init__: trading_unstack_data_frame = ")
                #
                #            print(trading_unstack_data_frame)

                #            trading_split_data_frame = trading_unstack_data_frame(['B'])
                #            print("TradeReport::__init__: trading_split_data_frame = ")
                #            print(trading_split_data_frame)

                # trading_sum_sorted = trading_groupby_data_frame.sort_values([Trade.Trade.get_column_heading_amount()], ascending=False)
                # print("TradeReport::__init__: trading_sum_sorted = ", trading_sum_sorted)

            else:
                self.logger.debug("trading_data_frame is incorrectly formatted/constructed/populated")
        except Exception as exception:
            # Utility.Utility.log_exception(exception, " Serious exception occurred")
            self.logger.warning('Exception occurred when adding data sample', exc_info=True)

    def calculate_sum(self, trading_sum_sorted):
        total_interval = 0

        try:
            if (self.utility.is_data_frame_data_format_valid(trading_sum_sorted)):
                total_interval = np.sum(trading_sum_sorted[Trade.Trade.get_column_heading_amount()])

                self.logger.info("total_interval = ")
                self.logger.info(total_interval)
            else:
                self.logger.debug("Unable to calculate total_interval. Set total_interval = 0 (default value)")
                total_interval = 0
        except Exception as exception:
            total_interval = 0
            self.logger.debug("Data format validation failed. Unable to process data.")
            self.logger.debug("Unable to calculate total_interval. Set total_interval = 0 (default value)")
            self.logger.warning('Exception occurred when calculating sum of DataFrame column', exc_info=True)

        return total_interval

    def display_incoming_outgoing_settled_per_workperiod(self):
        self.logger.info("display incoming outgoing daily: start")

        try:
            if (self.utility.is_data_frame_data_format_valid(self.trade_report_settled)):

                # total_interval = np.sum(trading_sum_sorted[Trade.Trade.get_column_heading_amount()])

                self.trade_report_settled = self.trade_report_settled.rename(
                    columns=Trade.Trade.get_buy_sell_instructions_readable(), copy=False)
                print("Incoming Outgoing settled daily")
                print(self.trade_report_settled)
            else:
                self.logger.debug("Unable to display Incoming & Outgoing settled daily")
        except Exception as exception:
            self.logger.debug("The display of Incoming & Outgoing settled daily failed.")
            self.logger.warning('Exception occurred when attempting to display Incoming & Outgoing settled daily',
                                exc_info=True)

        self.logger.info("display incoming outgoing daily: end")

    #    self.trade_report_settled = None
    #    self.ranking_by_trade_instructions_dict = {}


    def display_ranking(self):
        self.logger.info("display incoming outgoing daily: start")

        # ranking_by_trade_instructions_dict[buy_sell_unique] = trading_ranking_sum_sorted
        try:
            if (self.utility.is_dictionary_data_format_valid(self.ranking_by_trade_instructions_dict,
                                                             empty_permissible=False)):

                print("Ranking of entities by total amount settled per trading instruction:")

                trade_instructions_dict = Trade.Trade.get_buy_sell_instructions_readable()

                for key in self.ranking_by_trade_instructions_dict:
                    print()
                    print(trade_instructions_dict[key])
                    print(self.ranking_by_trade_instructions_dict[key])

            else:
                self.logger.debug("Passed dictionary has invalid data format")
        except Exception as exception:
            self.logger.debug("Display ranking failed.")
            self.logger.warning('Exception occurred when attempting to display ranking.', exc_info=True)

        self.logger.info("display incoming outgoing daily: end")

    def display_report(self):
        try:
            self.display_ranking()
            self.display_incoming_outgoing_settled_per_workperiod()
        except Exception as exception:
            self.logger.warning('Exception occurred when attempting to display report.', exc_info=True)