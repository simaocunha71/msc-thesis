def odd_length_sum(arr):
    n = len(arr)
    if n == 0:
        return 0
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            if j - i + 1 % 2 != 0:
                res += sum(arr[i:j+1])
    return res