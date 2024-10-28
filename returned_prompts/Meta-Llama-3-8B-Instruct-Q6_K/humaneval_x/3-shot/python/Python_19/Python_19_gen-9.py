    numbers_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numbers_list = list(map(lambda x: numbers_dict[x], numbers.split()))
    numbers_list.sort()
    return ' '.join(map(lambda x: list(numbers_dict.keys())[list(numbers_dict.values()).index(x)], numbers_list))
    # or
    return ' '.join(map(lambda x: list(numbers_dict.keys())[list(numbers_dict.values()).index(x)], sorted(map(lambda x: numbers_dict[x], numbers.split()))))  # one-liner version


