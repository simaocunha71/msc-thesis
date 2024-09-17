def odd_length_sum(arr):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    total = 0
    for i in range(n):
        for j in range(i, n):
            if (j - i + 1) % 2 != 0:
                total += prefix_sum[j + 1] - prefix_sum[i]
    return total