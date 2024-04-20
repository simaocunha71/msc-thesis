"""
Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.
assert check_monthnumber_number(6)==True
"""
from typing import Optional

def check_monthnumber_number(input_date: int) -> bool:
    if (input_date % 4 != 0 or input_date % 10 == 0 and input_date % 400 == 0):
        return True
    else:
        return False