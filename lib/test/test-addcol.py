# test-addcol.py
import pytest
from pyspark.sql import *
import pyspark.sql.functions as F

class TestAppendCol(object):

    def get_spark(self):
        self.spark = SparkSession.builder.getOrCreate()
        return self.spark

    def test_with_status(self):
        source_data = [
            ("paula", "white", "paula.white@example.com"),
            ("john", "baer", "john.baer@example.com")
        ]
        source_df = get_spark().createDataFrame(
            source_data,
            ["first_name", "last_name", "email"]
        )

        actual_df = source_df.withColumn("status", F.lit("checked"))

        expected_data = [
            ("paula", "white", "paula.white@example.com", "checked"),
            ("john", "baer", "john.baer@example.com", "checked")
        ]
        expected_df = get_spark().createDataFrame(
            expected_data,
            ["first_name", "last_name", "email", "status"]
        )

    assert(True == True)