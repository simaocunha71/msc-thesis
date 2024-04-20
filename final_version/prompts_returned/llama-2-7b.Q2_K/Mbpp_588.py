"""
Write a python function to find the difference between largest and smallest value in a given list.
assert big_diff([1,2,3,4]) == 3
"""
big_diff = lambda x: max(x) - min(x)
assert big_diff([1,2,3,4]) == 3
