    numbers_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    num_list = numbers.split()
    sorted_num_list = sorted([numbers_dict[num] for num in num_list])
    return ' '.join([list(numbers_dict.keys())[list(numbers_dict.values()).index(num)] for num in sorted_num_list])
