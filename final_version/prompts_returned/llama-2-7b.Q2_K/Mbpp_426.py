"""
Write a function to filter odd numbers.
assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]
"""

def filter_oddnumbers(numbers):
    """filter the odd number"""
    return [x for x in numbers if x%2 == 1]