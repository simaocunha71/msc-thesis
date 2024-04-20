"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""
from typing import Optional

def last(arr: [int], key: int) -> int:
    for i in range(len(arr)):
        if arr[i] == key: return i