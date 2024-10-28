    numbers = numbers.split()
    numbers.sort(key=lambda x: ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'].index(x))
    return ' '.join(numbers)


