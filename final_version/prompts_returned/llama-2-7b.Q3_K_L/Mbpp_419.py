"""
Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
"""

def round_and_sum(nums):
    """
    :param nums: An iterable (e.g., a list) of numbers that you want to sum and output the result as a string in Python.
    :return: A single string containing the sum of all the elements multiplied by the total number of elements. The number should be rounded at two decimal places.
    """
    round_sum = 0
    
    for n, r in zip(nums, map(round, nums)): # create a list of tuples from the iterable with each tuple containing the number and its respective rounded version (from the map function)
        print(n, ':', r)
        round_sum += r * len(nums)
    return str(round_sum / 1024.99)