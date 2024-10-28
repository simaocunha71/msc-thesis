def odd_length_sum(arr):
    n = len(arr)
    total = 0
    for i in range(1 << n):
        sub_sum = 0
        for j in range(n):
            if i & (1 << j):
                sub_sum += arr[j]
        total += sub_sum
    return total