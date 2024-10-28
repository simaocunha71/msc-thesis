from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a mapping from words to numbers
    word_to_num = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    # Split the input string into a list of words
    words = numbers.split()

    # Convert each word to its corresponding number
    numbers = [word_to_num[word] for word in words]

    # Sort the numbers
    numbers.sort()

    # Convert each number back to its corresponding word
    sorted_words = [list(word_to_num.keys())[list(word_to_num.values()).index(num)] for num in numbers]

    # Join the sorted words back into a string
    sorted_numbers = ' '.join(sorted_words)

    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'