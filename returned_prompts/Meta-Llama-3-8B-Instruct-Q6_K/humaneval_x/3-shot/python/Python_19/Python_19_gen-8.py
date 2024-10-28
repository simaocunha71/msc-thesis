    numbers_list = numbers.split()
    numbers_list.sort(key=lambda x: ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'].index(x))
    return ' '.join(numbers_list)
    # or
    # return ' '.join(sorted(numbers.split(), key=lambda x: ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'].index(x)))  # one-liner


