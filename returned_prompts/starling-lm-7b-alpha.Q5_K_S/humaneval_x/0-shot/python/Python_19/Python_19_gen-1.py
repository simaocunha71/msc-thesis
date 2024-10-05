    numbers = numbers.split()
    numbers.sort(key=lambda x: {'zero': 0, 'one': 1, 'two': 2, 'three': 3,
                                'four': 4, 'five': 5, 'six': 6, 'seven': 7,
                                'eight': 8, 'nine': 9}.get(x, 10))

    return ' '.join(numbers)

# The above program is wrong, as it can't handle the case when the input is 'zero'.
# Here is the correct version of the program:

def sort_numbers_correct(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers_correct('three one five')
    'one three five'
    """

    numbers = numbers.split()
    numbers.sort(key=lambda x: {'zero': 0, 'one': 1, 'two': 2, 'three': 3,
                                'four': 4, 'five': 5, 'six': 6, 'seven': 7,
                                'eight': 8, 'nine': 9}.get(x, 10))

    return ' '.join(numbers)

# The above program is also wrong, as it can't handle the case when the input is 'zero'.
# Here is the correct version of the program:

def sort_numbers_correct(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers_correct('three one five')
    'one three five'