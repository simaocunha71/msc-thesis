def odd_length_sum(arr):
    total = 0
    n = len(arr)
    for length in range(1, n+1, 2):
        for i in range(n-length+1):
            total += sum(arr[i:i+length])
    return total