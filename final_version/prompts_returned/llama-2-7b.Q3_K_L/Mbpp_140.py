"""
Write a function to flatten the list of lists into a single set of numbers.
assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
"""
from typing import List

def extract_singly(list:List[tuple] ) -> list:
    return [item[0] for item in list]