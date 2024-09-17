def odd_length_sum(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if j - i == 1:
                total += arr[i]
            elif j - i % 2 != 0:
                total += sum(arr[i:j])
    return total