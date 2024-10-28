
def interleave_lists(a, b, c):
    return [val for pair in zip(a, b, c) for val in pair]
"""
zip() function is used to combine the lists a, b, c into a list of tuples, where each tuple contains one element from each list.
Then we use a list comprehension to flatten the list of tuples into a single list.
"""

