def odd_length_sum(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        res += ((i+1)*(n-i)+1)//2*arr[i]
    return res