"""
TASK
----
Edit the below functions so that they actually implement the desired functionality.
"""
import numpy as np
import pandas as pd

def convert_radians_to_degrees(rad: float) -> float:
    """
    Convert an angle from radians to degrees.

    Parameters:
        rad (float): Angle in radians.

    Returns:
        float: Angle in degrees.
    """
    return rad * (180 / np.pi)

def sort_list(numbers: list, order: str) -> list:
    """
    Sort a list of numbers based on the specified order.

    Parameters:
        numbers (list): List of numbers to sort.
        order (str): Sorting order - 'asc', 'desc', or 'none'.

    Returns:
        list: Sorted list in ascending order if 'asc', descending order if 'desc',
              or the original list if 'none'.
    """
    pass

def count_vowels(word: str) -> int:
    """
    Count the number of vowels in a word.

    Parameters:
        word (str): The word to count vowels in.

    Returns:
        int: Number of vowels in the word.
    """
    pass

def hide_credit_card_number(card_number: str) -> str:
    """
    Hide all but the last four digits of a credit card number.

    Parameters:
        card_number (str): The credit card number.

    Returns:
        str: The credit card number with all but the last four digits hidden.
    """
    pass

def equal_xo(s: str) -> bool:
    """
    Check if the number of 'X's and 'O's in a string are equal.

    Parameters:
        s (str): The string to check.

    Returns:
        bool: True if the counts of 'X's and 'O's are equal, False otherwise.
              Also returns True if there are no 'X's or 'O's.
    """
    pass

def calculator(a: int, operator: str, b: int) -> float:
    """
    Perform a calculation with two integers and an operator.

    Parameters:
        a (int): First integer.
        operator (str): Mathematical operator ('+', '-', '*', '/').
        b (int): Second integer.

    Returns:
        float: Result of the calculation.
    """
    pass

def apply_discount(price: int, discount: int) -> float:
    """
    Calculate the price after applying a discount.

    Parameters:
        price (int): Original price.
        discount (int): Discount percentage.

    Returns:
        float: Price after discount.
    """
    pass

def filter_numbers(mixed_list: list) -> list:
    """
    Filter out non-integer elements from a list.

    Parameters:
        mixed_list (list): List containing integers and strings.

    Returns:
        list: List containing only integers.
    """
    pass

def repeat_characters(s: str) -> str:
    """
    Repeat each character in a string.

    Parameters:
        s (str): The string to process.

    Returns:
        str: String with each character repeated.
    """
    pass

def to_uppercase(s: str) -> str:
    """
    Convert all lowercase characters in a string to uppercase.

    Parameters:
        s (str): The string to convert.

    Returns:
        str: String with all lowercase characters converted to uppercase.
    """
    pass

def add_dots(s: str) -> str:
    """
    Add dots between each character in a string.

    Parameters:
        s (str): The string to process.

    Returns:
        str: String with dots added between characters.
    """
    pass

