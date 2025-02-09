import pytest
from pyanalytics.task1 import (
    convert_radians_to_degrees,
    sort_list,
    count_vowels,
    hide_credit_card_number,
    equal_xo,
    calculator,
    apply_discount,
    filter_numbers,
    repeat_characters,
    to_uppercase,
    add_dots
)

def test_convert_radians_to_degrees():
    assert convert_radians_to_degrees(0) == 0
    assert convert_radians_to_degrees(3.14159) == pytest.approx(180, 0.01)
    assert convert_radians_to_degrees(1) == pytest.approx(57.2958, 0.01)

def test_sort_list():
    assert sort_list([10, 3, 5, 1, 9, 2, 8, 4, 7, 6], 'asc') == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sort_list([10, 3, 5, 1, 9, 2, 8, 4, 7, 6], 'desc') == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert sort_list([10, 3, 5, 1, 9, 2, 8, 4, 7, 6], 'none') == [10, 3, 5, 1, 9, 2, 8, 4, 7, 6]

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("world") == 1
    assert count_vowels("bcdfg") == 0

def test_hide_credit_card_number():
    assert hide_credit_card_number("1234567812345678") == "************5678"
    assert hide_credit_card_number("1234") == "1234"
    assert hide_credit_card_number("123456") == "**3456"

def test_equal_xo():
    assert equal_xo("xxoo") == True
    assert equal_xo("xoxo") == True
    assert equal_xo("xxo") == False

def test_calculator():
    assert calculator(1, '+', 1) == 2
    assert calculator(2, '*', 3) == 6
    assert calculator(4, '/', 2) == 2

def test_apply_discount():
    assert apply_discount(100, 10) == 90
    assert apply_discount(200, 25) == 150
    assert apply_discount(50, 0) == 50

def test_filter_numbers():
    assert filter_numbers([1, 'a', 2, 'b', 3]) == [1, 2, 3]
    assert filter_numbers(['x', 'y', 'z']) == []
    assert filter_numbers([1, 2, 3]) == [1, 2, 3]

def test_repeat_characters():
    assert repeat_characters("abc") == "aabbcc"
    assert repeat_characters("123") == "112233"
    assert repeat_characters("") == ""

def test_to_uppercase():
    assert to_uppercase("hello") == "HELLO"
    assert to_uppercase("WORLD") == "WORLD"
    assert to_uppercase("HeLLo WoRLD") == "HELLO WORLD"

def test_add_dots():
    assert add_dots("abc") == "a.b.c"
    assert add_dots("123") == "1.2.3"
    assert add_dots("") == ""
