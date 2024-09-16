def round_and_sum(numbers):
    total = sum([round(x) for x in numbers])
    return total * len(numbers)