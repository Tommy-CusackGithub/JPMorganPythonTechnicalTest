#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Mar - Apr 2017

@author: Tommy Cusack
"""
import logging
import pandas as pd


class Utility:
    logger = logging.getLogger(__name__)

    @classmethod
    def is_data_frame_data_format_valid(cls, df: pd.DataFrame):
        """
        Validates data formats of pd.DataFrame's before said pd.DataFrame's are passed to other methods

        Args:
            df (pd.DataFrame): DataFrame basic integrity checks for data format validity. Shouldn't be None.
        Returns:
            bool: True if successful, False otherwise.
        """
        data_format_valid = False

        try:
            if df is not None:
                if type(df) is pd.DataFrame:
                    if len(df) > 0:
                        if len(df.columns) > 0:
                            data_format_valid = True
                        else:
                            cls.logger.info("Expected len(df.columns) > 0."
                                            , " len(df.columns) == 0 "
                                            , " implies inability to process data")
                    else:
                        cls.logger.info("Expected len(df) > 0. len(df) == 0 implies unable to process data")
                else:
                    cls.logger("Expected df to be of type DataFrame. Unable to process data")
            else:
                cls.logger("DataFrame cannot be None. Unable to process data")
        except Exception as exception:
            cls.logger.warning('Exception occurred when validating DataFrame', exc_info=True)

        return data_format_valid

    @classmethod
    def is_dictionary_data_format_valid(cls, dictionary: dict, empty_permissible: bool):
        """
        Validates data formats of dict's before said dict's are passed to other methods

        Args:
            dictionary (dict): dict basic integrity checks for data format validity. Shouldn't be None.
        Returns:
            bool: True if successful, False otherwise.
        """
        data_format_valid = False

        try:
            if dictionary is not None:
                if type(dictionary) is dict:
                    if (not empty_permissible) and len(dictionary) == 0:
                        data_format_valid = False
                        cls.logger.info("len(dictionary) == 0 is true, expected len(dictionary) > 0.")
                    else:
                        data_format_valid = True
                    cls.logger.info("data_format_valid = %s", data_format_valid)
                else:
                    cls.logger("Expected dictionary to be of type dict. Unable to process data")
            else:
                cls.logger("dictionary cannot be None. Unable to process data")
        except Exception as exception:
            cls.logger.warning('Exception occurred when validating dictionary', exc_info=True)

        return data_format_valid

