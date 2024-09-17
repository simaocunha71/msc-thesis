import unittest
def frequency(lst, target):
    """
    Count the number of occurrences of a number in a given list.
    """

    # Initialize the count to 0
    count = 0
    # Iterate through the list and compare each element to the target
    for item in lst:
        if item == target:
            count += 1
    # Return the count
    return count