"""
    Contains the Column class
"""

from __future__ import annotations
from typing import List, Dict, Any, Callable, TypeVar

T = TypeVar('T')


class Column():
    """
        The Column class represents a column in a Dataset. Each column is
        an attribute in the data set and a row is an entry with a value for each
        column.
    """

    def __init__(self,
                 column_name: str,
                 value_generator: Callable[Dict[str, Any], T]):
        """
        Constructor for the Column class

        Parameters
        __________
        column_name : str
            The name of this column

        value_generator : Callable[Dict[str, Any]]
            The a callable (function) to produce a the next value for
            this column
        """
        self.column_name = column_name
        self._value_generator = value_generator

    def create_value(self,
                     row_number: int,
                     previous_row_values: Dict[str, Any]) -> T:
        """
        Produces this column's next value

        Uses the object's value_generator to produce a new value for this column

        Parameters
        __________
        previous_row_values : Dict[str, Any]
            The previous values for the row this value is being created for

        Returns
        _______
        T
            Whatever value this object's value_generator produces
        """
        return self._value_generator(
            row_number=row_number,
            previous_row_values=previous_row_values)
