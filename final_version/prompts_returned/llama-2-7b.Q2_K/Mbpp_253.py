"""
Write a python function that returns the number of integer elements in a given list.
assert count_integer([1,2,'abc',1.2]) == 2
"""

def count_integer(lst):
    count = 0
    for n in lst:
        try:
            if type(n) is int:
                count += 1
                break
        except ValueError: pass
    return count
