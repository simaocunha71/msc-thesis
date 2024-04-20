"""
Write a python function to find the last digit of a given number.
assert last_Digit(123) == 3
"""
from typing import List, Any
def last_Digit(number: Any = None):
    if not number is None:
        digits : int
        for i in range(len(str(number))-1,-1,-1):
            if str(int(number[i])) in ['0', '9']:
                digits = i+1
    else:
        digits = 0
    return digits
if __name__ == '__main__':
    print('last_Digit(123)=%s' % last_Digit(123))