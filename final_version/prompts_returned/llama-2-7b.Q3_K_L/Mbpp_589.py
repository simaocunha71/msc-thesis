"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""
from typing import List

def perfect_squares(start:int,stop:int):
    return [number for number in range(start , stop + 1)]
    # print(perfect_squares(3, 10))
