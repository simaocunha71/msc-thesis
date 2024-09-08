def sum_list(a, b):
    return [x+y for x, y in zip(a, b)]

assert sum_list([10,20,30],[15,25,35])==[25,45,65]
"""
Explanation:
The function sum_list takes two lists as input. Using the zip function, it creates pairs of elements from the two lists at the corresponding indices. For each pair, it adds the two numbers together and adds the result to a new list. The new list is then returned.
"""

