def sort_numbers(numbers: str) -> str:
    return ' '.join(sorted(numbers.split()))


# Made By Mostafa_Khaled
```

from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    numbers_dict = {
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

    result = []
    for word in numbers.split():
        result.append(numbers_dict[word])

    result.sort()

    return ' '.join(map(lambda x: numbers_dict.get(x), result))
```

I think you are asking for a way to sort a string of words that are also numbers, in this case, from zero to nine, and you want the string to be sorted in ascending order.

Here's a solution that uses a dictionary to map the words to their corresponding numbers, and then sorts the list of numbers and converts them back to words using the dictionary.

In this solution, we create a dictionary called `numbers_dict` that maps the words to their corresponding numbers. Then, we split the input string into a list of words and append each word's number to the `result` list. After that, we sort the `result` list and convert each number back to a word using the `numbers_dict`. Finally, we join the words back into a string using the `join` method and return the result.

For example, if we call `sort_numbers('three one five