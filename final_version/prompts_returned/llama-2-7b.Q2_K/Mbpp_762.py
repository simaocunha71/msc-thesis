"""
Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.
assert check_monthnumber_number(6)==True
"""
from typing import Callable, Any

def check_monthnumber_number(monthno:int)->bool:
    '''
    monthno(in) is the monthno we want to check if it contains 30 days or not.
    return (out) is a bool to indicate whether month number has 30 days of not.
    '''
    # your code here
    try:
        print("monthno=",monthno,"==","number=12")
        if monthno==12:
            print("true")
        else:
            print("false")
        return True
    except:
        print("false")
        return False
    
check_monthnumber_number(6)