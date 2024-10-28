def odd_length_sum(arr):
    n = len(arr)
    result = 0
    for i in range(n):
        result += ((i+1)*(n-i)+1)//2*arr[i]
    return result