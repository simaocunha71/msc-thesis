"""
Write a function to check whether the given month number contains 31 days or not.
assert check_monthnumb_number(5)==True
"""
from typing import Callable, List, Optional, Union


def check_date(month: int, year: int):
    """Checks if an inputted date is valid according to the format of a date in mm/dd/yyyy."""
    # type: (int, int) -> bool
    return month > 2 and month < 14 and year >= 0 and year <= 9999


def check_monthnumb_number(month: int):
    """Checks if the month number contains 31 days or not."""
    # type: (int) -> bool
    return (check_date(month, 2022)) and month in [1, 3, 5, 7, 8, 10, 12]


def check_date_number(year: int):
    """Checks if an inputted date is valid according to the format of a date in mm/dd/yyyy."""
    # type: (int) -> bool
    return year >= -950 and year <= 2799


def check_date_number2(year: int):
    """Checks if an inputted date is valid according to the format of a date in mm/dd/yyyy."""
    # type: (int) -> bool
    return check_monthnumb_number(1) and year >= 0 and year <= 9999


def check_all_date() -> list[str]:
    """Checks if all dates are valid according to the format of a date in mm/dd/yyyy."""
    # type: () -> [str]
    daylist = []
    for months in range(1, 13):
        year = input("Please enter the starting year as an integer. Example 2022.\n")  # type: str
        month_number = input(f"Please enter the month number of that start date. Examples {str(check_monthnumb_number(1))} and {str(check_monthnumb_number(5))}.\n")  # type: int
        daylist.append(f'{months}-{month_number}-2022')
    return daylist


