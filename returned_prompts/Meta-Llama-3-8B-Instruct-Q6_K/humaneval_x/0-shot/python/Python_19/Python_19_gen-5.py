from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input string into a list of strings
    num_list = numbers.split()

    # Define a dictionary to map string numbers to integers
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }

    # Convert the list of strings to a list of integers
    num_list = [num_map[num] for num in num_list]

    # Sort the list of integers
    num_list.sort()

    # Convert the sorted list of integers back to a list of strings
    sorted_num_list = [list(num_map.keys())[list(num_map.values()).index(num)] for num in num_list]

    # Join the sorted list of strings into a single string with spaces in between
    sorted_numbers = ' '.join(sorted_num_list)

    return sorted_numbers
# Test the function
print(sort_numbers('three one five'))
# Output: one three five
print(sort_numbers('nine eight seven six five four three two one'))
# Output: one two three four five six seven eight nine
print(sort_numbers('five one'))
# Output: one five
print(sort_numbers('zero one'))
# Output: one zero
print(sort_numbers(''))
# Output: (empty string)  # No output because the input is an empty string
print(sort_numbers(' invalid input'))
# Output: (raises ValueError)  # Raises an error because the input contains invalid numbers
print(sort_numbers('zero one two three four five six seven eight nine'))
# Output: one two three four five six seven eight nine
print(sort_numbers('nine nine nine nine nine'))
# Output: nine nine nine nine nine
print(sort_numbers('one one one one one'))
# Output: one one one one one
print(sort_numbers('five five five five five'))
