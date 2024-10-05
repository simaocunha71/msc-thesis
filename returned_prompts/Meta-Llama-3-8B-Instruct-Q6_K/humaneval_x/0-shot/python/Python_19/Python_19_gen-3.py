from typing import List

def sort_numbers(numbers: str) -> str:
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    num_list = numbers.split()
    sorted_num_list = sorted([num_dict[num] for num in num_list])
    sorted_num_str = ' '.join([str(num_dict[num]) for num in num_list if str(num_dict[num]) == str(sorted_num_list[i])])
    return ' '.join(sorted_num_str.split())
# Test the function
print(sort_numbers('three one five'))
print(sort_numbers('eight nine seven'))
print(sort_numbers('zero five three two'))  # Test for the case of multiple same numbers
print(sort_numbers('six seven eight nine ten'))  # Test for the case of numbers greater than nine
print(sort_numbers('nine eight seven six five four three two one zero'))  # Test for the case of all numbers
print(sort_numbers('one'))  # Test for the case of single number
print(sort_numbers(''))  # Test for the case of empty string
print(sort_numbers('zero one two'))  # Test for the case of multiple numbers
print(sort_numbers('zero'))  # Test for the case of single number
print(sort_numbers('five six seven eight nine'))  # Test for the case of multiple numbers
print(sort_numbers('two three four five six seven eight nine ten'))  # Test for the case of multiple numbers
print(sort_numbers('nine seven five three one'))  # Test for the case of multiple numbers
print(sort_numbers('one two three four five six seven eight nine'))  # Test for the case of multiple numbers
print(sort_numbers('zero one two three four five six seven eight nine ten'))  # Test for the case of multiple numbers
print(sort_numbers('nine eight seven six five four three two one'))  # Test for the case of multiple numbers
print(sort_numbers('one two three four five six seven eight nine ten eleven'))  # Test for the case of multiple numbers
print(sort_numbers('zero one two three four five six seven eight nine ten eleven twelve'))  # Test for the case of multiple numbers
print(sort_numbers('one'))  # Test for the case of single number
print(sort_numbers('zero