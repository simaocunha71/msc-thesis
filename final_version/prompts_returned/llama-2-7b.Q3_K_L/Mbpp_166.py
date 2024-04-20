"""
Write a function that counts the number of pairs of integers in a list that xor to an even number.
assert find_even_pair([5, 4, 7, 2, 1]) == 4
"""
from typing import List

def find_even_pair(arr: List[int]) -> int:
    sum = len(arr) // 2
    return sum - ((sum + 1) % sum)
