def odd_length_sum(arr):
    n = len(arr)
    total_sum = 0
    for i in range(n):
        for j in range(i, n):
            if (j - i + 1) % 2 != 0:
                total_sum += sum(arr[i:j+1])
    return total_sum