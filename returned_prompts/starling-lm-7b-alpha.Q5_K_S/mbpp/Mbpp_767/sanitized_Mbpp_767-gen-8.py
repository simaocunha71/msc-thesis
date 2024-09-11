def get_pairs_count(numbers, sum):
    return sum(map(lambda x: len([1 for y in numbers if y == sum-x]), numbers))