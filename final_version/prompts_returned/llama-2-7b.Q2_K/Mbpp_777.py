"""
Write a python function to find the sum of non-repeated elements in a given list.
assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""
from typing import Optional

def find_sum(l: list[int], start=0) -> int:
    prev = l[start]

    def check_if_found(curr):
        if curr == prev + 1:
            return True, curr
        else:
            return False, None
    
    while len(l) > 2 and not check_if_found(*[i for i in l[start:]])[0]:
        prev += 1
        l.remove(prev)
    
    assert (len(l) == start + 1), f"{l} is empty!"

    return sum([i for i in l if len(find_sum(l, start)) > 2])
