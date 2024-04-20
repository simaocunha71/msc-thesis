"""
Write a function that takes in two numbers and returns a tuple with the second number and then the first number.
assert swap_numbers(10,20)==(20,10)
"""
from typing import *
def swap_numbers(a:int, b: int)->tuple[int, int]:
	return (b, a) 
	#return tuple of second number and then first number
swap_numbers(456,789)