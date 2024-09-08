def odd_length_sum(arr):
    sum = 0
    n = len(arr)
    for i in range(n):
        for j in range(i, n, 2):
            sum += sum(arr[i:j+1])
    return sum