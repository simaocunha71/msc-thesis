def odd_length_sum(arr):
    total = 0
    for start in range(len(arr)):
        for length in range(1, len(arr) - start + 1, 2):
            total += sum(arr[start:start + length])
    return total