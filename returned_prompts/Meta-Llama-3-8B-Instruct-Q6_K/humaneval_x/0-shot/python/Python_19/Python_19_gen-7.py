from typing import List

def sort_numbers(numbers: str) -> str:
    num_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    num_list = [num_map[num] for num in numbers.split()]
    num_list.sort()
    return ' '.join([key for key, value in sorted(num_map.items(), key=lambda item: item[1]) if value in num_list])  # Sort numbers and then get the corresponding keys from the dictionary
    # Sort numbers and then get the corresponding keys from the dictionary

print(sort_numbers('three one five'))  # Output: 'one three five'  # Test the function
print(sort_numbers('nine eight seven'))  # Output: 'seven eight nine'  # Test the function
print(sort_numbers('zero five one'))  # Output: 'one five zero'  # Test the function
print(sort_numbers('six four two'))  # Output: 'two four six'  # Test the function
print(sort_numbers('nine five three'))  # Output: 'three five nine'  # Test the function
print(sort_numbers('eight seven six'))  # Output: 'six seven eight'  # Test the function
print(sort_numbers('five four three'))  # Output: 'three four five'  # Test the function
print(sort_numbers('two one zero'))  # Output: 'zero one two'  # Test the function
print(sort_numbers('nine eight seven six five four three two one zero'))  # Output: 'zero one two three four five six seven eight nine'  # Test the function
print(sort_numbers('zero'))  # Output: 'zero'  # Test the function
print(sort_numbers('one'))  # Output: 'one'  # Test the function
print(sort_numbers('two'))  # Output: 'two'  # Test the function
print(sort_numbers('three'))  # Output: 'three'  # Test the function
print(sort_numbers('four'))  # Output: 'four'  # Test the function
print(sort_numbers('five'))  # Output: 'five'  # Test the function
print(sort_numbers('six'))  # Output: 'six'  # Test the function
