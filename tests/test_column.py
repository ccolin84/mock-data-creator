"""
    Unit tests for Column class
"""

import unittest
from mockdataset.column import Column


def test_value_generator_fn(row_number, previous_row_values):
    """
    test value generator function for the test column
    """
    return 10


class TestColumn(unittest.TestCase):
    """
        Unit tests for Column class
    """

    def setUp(self):
        """
        test set up
        """
        self.column = Column(
            column_name="test_column",
            value_generator=test_value_generator_fn)

    def test_init(self):
        """
        test that Column initializes correctly
        """
        self.assertEqual(self.column.column_name, "test_column")

    def test_create_value(self):
        """
        test that Column call its create_value function correctly
        """
        test_row_number = 0
        test_previous_row_values = []

        column_next_value = self.column.create_value(
            row_number=test_row_number,
            previous_row_values=test_previous_row_values)

        expected_next_value = test_value_generator_fn(
            row_number=test_row_number,
            previous_row_values=test_previous_row_values)

        self.assertEqual(column_next_value, expected_next_value)
