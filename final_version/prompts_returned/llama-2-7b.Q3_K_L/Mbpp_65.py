"""
Write a function to flatten a list and sum all of its elements.
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
"""

def recursive_list_sum(l):
    if not isinstance(l,list):return l
    return sum([item + recursive_list_sum(item) for item in l])
print(recursive_list_sum([1, 2, [3,4],[5,6]]))