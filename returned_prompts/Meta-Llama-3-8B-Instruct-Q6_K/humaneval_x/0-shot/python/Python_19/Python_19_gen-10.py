from typing import List


def sort_numbers(numbers: str) -> str:
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    numbers_list = numbers.split()
    sorted_numbers = sorted([num_map[num] for num in numbers_list])
    return ' '.join([list(num_map.keys())[list(num_map.values()).index(num)] for num in sorted_numbers])
# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output: 'seven eight nine'  # Input is a space-delimited string of numberals from 'zero' to 'nine'. Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'. Return the string with numbers sorted from smallest to largest
>>> sort_numbers('three one five')
'one three five'
>>> sort_numbers('nine eight seven')
'seven eight nine'
>>> sort_numbers('one zero four')
'four one zero'
>>> sort_numbers('nine nine eight')
'eight nine nine'
>>> sort_numbers('zero five five')
'five five zero'
>>> sort_numbers('nine nine nine')
'nine nine nine'
>>> sort_numbers('two two two')
'two two two'
>>> sort_numbers('seven seven seven')
'seven seven seven'
>>> sort_numbers('one two three')
'one two three'
>>> sort_numbers('zero one zero')
'one zero zero'
>>> sort_numbers('nine nine nine')
'nine nine nine'
>>> sort_numbers('six six six')
'six six six'
>>> sort_numbers('eight eight eight')
'eight eight eight'
>>> sort_numbers('five five five')
'five five five'
>>> sort_numbers('three three three')
'three three three'
>>> sort_numbers('four four four')
'four four four'
>>> sort_numbers('seven seven seven')
'seven seven seven'
>>> sort_numbers('eight eight eight')
'eight eight eight'
>>> sort_numbers('six six six')
'six six six'
>>> sort_numbers('nine nine nine')
'nine nine nine'
>>> sort_numbers('two two two')
'two two two'
>>> sort_numbers