"""
Write a function to find cubes of individual elements in a list.
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""

def cube_nums(numbers):
    """
    :param numbers: list or array of numbers to find cubes in.
    :type numbers: iterable of int
    :return: list of cubed elements found in the input array.
    :rtype: iterable of int
    """
    numbers_list = []

    for number in numbers:
        if number < 0:
            raise ValueError('Array elements can\'t be negative')
        numbers_list.append(number**3)
        
    return numbers_list