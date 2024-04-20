"""
Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple.
assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
"""
from typing import List
def split_two_parts(l:List[int], k: int) -> Tuple[List[int], List[int]] :
    return (split_at_k(k, l), split_at_k(-k, l))
def split_at_k(k: int, l: list):
    return sorted(l[:-len(l)%k+1]) + sorted(l[len(l)/2::len(l)+1:])