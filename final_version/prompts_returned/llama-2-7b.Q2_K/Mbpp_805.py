"""
Write a function that returns the list in a list of lists whose sum of elements is the highest.
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
"""

def sum_of_elements(list):
    # return the greatest sum of elements in a list. In this case the greatest one is when we have all integers and the sum is the largest possible one.
    return max([sum(l) for l in list])