    number_to_str = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    str_to_number = {v: i for i, v in enumerate(number_to_str)}

    numbers_split = numbers.split()
    numbers_split.sort(key=lambda x: str_to_number[x])

    return ' '.join(numbers_split)


