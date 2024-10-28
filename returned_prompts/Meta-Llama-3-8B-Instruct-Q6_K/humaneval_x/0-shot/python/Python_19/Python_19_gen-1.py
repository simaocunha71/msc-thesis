    # Convert the input string into a list of integers
    numbers_list = []
    for num_str in numbers.split():
        num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
        numbers_list.append(num_dict[num_str])

    # Sort the list
    numbers_list.sort()

    # Convert the list back to a string
    result = ' '.join(str(num) for num in numbers_list)
    return result
    # Test the function
    print(sort_numbers('three one five'))  # Output: 'one three five'







# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'







# Test the function
print(sort_numbers('six five eight'))  # Output: 'five six eight'







# Test the function
print(sort_numbers('nine eight seven'))  # Output: 'seven eight nine'







# Test the function
print(sort_numbers('zero four two'))  # Output: 'two four zero'







# Test the function
print(sort_numbers('one nine three'))  # Output: 'one three nine'







# Test the function
print(sort_numbers('eight six five'))  # Output: 'five six eight'







# Test the function
print(sort_numbers('seven three one'))  # Output: 'one three seven'







# Test the function
print(sort_numbers('five four two'))  # Output: 'two four five'







# Test the function
print(sort_numbers('nine eight six'))  # Output: 'six eight nine'







# Test the function
print(sort_numbers('zero seven five'))  # Output: 'five seven zero'







# Test the function
print(sort_numbers('three two one'))  # Output: 'one two three'







# Test the function
print(sort_numbers('eight nine seven'))  # Output: 'seven eight nine'







# Test the function
print(sort_numbers('four six five'))  # Output: 'five six four'







# Test the function
print(sort_numbers('nine five three'))  # Output: 'three five nine'







# Test the function
print(sort_numbers('seven eight six'))  # Output: 'six seven eight'







# Test the function