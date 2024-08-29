"""
Here is the Python code for the function.

def get_median(list1, list2, n):
    merged_list = sorted(list1 + list2)
    return (merged_list[n - 1] + merged_list[n]) / 2

The function works by merging the two lists, sorting them, and then finding the median by averaging the two middle numbers. If the list size is odd, there is one middle number, otherwise there are two middle numbers.
"""

