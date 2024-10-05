    numbers_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    input_list = numbers.split()
    sorted_list = sorted([numbers_dict[i] for i in input_list])
    output_list = [list(numbers_dict.keys())[list(numbers_dict.values()).index(i)] for i in sorted_list]
    return ' '.join(output_list)


