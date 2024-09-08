def zero_count(arr):
    num_zeroes = sum(1 for x in arr if x == 0)
    num_non_zeroes = len(arr) - num_zeroes
    ratio = num_zeroes / num_non_zeroes if num_non_zeroes != 0 else 0
    return ratio