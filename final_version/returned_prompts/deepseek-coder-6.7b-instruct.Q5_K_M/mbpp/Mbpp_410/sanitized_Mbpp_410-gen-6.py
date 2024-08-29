def min_val(lst):
    numbers = [i for i in lst if isinstance(i, (int, float))]
    return min(numbers)