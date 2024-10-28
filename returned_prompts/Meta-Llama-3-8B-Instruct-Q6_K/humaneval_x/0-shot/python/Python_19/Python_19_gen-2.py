    # Split the input string into a list of numbers
    numbers_list: List[str] = numbers.split()

    # Define a dictionary to map string numbers to their integer values
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }

    # Convert the list of string numbers to a list of integer numbers
    numbers_list_int: List[int] = [number_map[num] for num in numbers_list]

    # Sort the list of integer numbers
    numbers_list_int.sort()

    # Convert the sorted list of integer numbers back to a list of string numbers
    numbers_list_sorted: List[str] = [list(number_map.keys())[list(number_map.values()).index(num)] for num in numbers_list_int]

    # Join the sorted list of string numbers back into a string
    sorted_numbers: str = ' '.join(numbers_list_sorted)

    return sorted_numbers
    # Return the string with numbers sorted from smallest to largest
    # >>> sort_numbers('three one five')
    # 'one three five'
    # Test cases
    # >>> sort_numbers('zero two four six')
    # 'two four six zero'
    # >>> sort_numbers('five three one seven')
    # 'one three five seven'
    # >>> sort_numbers('nine eight seven')
    # 'seven eight nine'  # no 'zero' or 'one'
    # >>> sort_numbers('one')
    # 'one'
    # >>> sort_numbers('zero')
    # 'zero'
    # >>> sort_numbers('zero one two three four five six seven eight nine')
    # 'zero one two three four five six seven eight nine'
    # >>> sort_numbers('nine eight seven six five four three two one zero')
    # 'zero one two three four five six seven eight nine'
    # >>> sort_numbers('nine nine nine nine nine')
    # 'nine nine nine nine nine'
    # >>> sort_numbers('zero zero zero zero zero')
    # 'zero zero zero zero zero'
    # >>> sort_numbers('')
    # ''
    # >>> sort_numbers('  ')
    # ''
    # >>> sort_numbers('zero one two three four five six seven eight nine ten')
    # 'zero one two three four five