def check_distinct(tup):
    if len(tup) == len(set(tup)):
        return True
    else:
        return False

print(check_distinct((1, 4, 5, 6, 1, 4)))  # False

"""
Write a function that takes a list of integers and returns a dictionary where the keys are the integers and the values are the number of occurrences of the integer in the list.

assert count_elements([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
"""

