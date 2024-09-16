def odd_length_sum(arr):
    return sum(x for i, x in enumerate(arr) if i % 2)