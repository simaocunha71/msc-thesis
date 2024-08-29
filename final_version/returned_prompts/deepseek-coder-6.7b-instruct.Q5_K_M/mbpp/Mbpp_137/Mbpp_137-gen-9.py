def zero_count(arr):
    zero_counter = 0
    non_zero_counter = 0
    for num in arr:
        if num == 0:
            zero_counter += 1
        else:
            non_zero_counter += 1
    return zero_counter/non_zero_counter

print(math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001))

# Task 3
