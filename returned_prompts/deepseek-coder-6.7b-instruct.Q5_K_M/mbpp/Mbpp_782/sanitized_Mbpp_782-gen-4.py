def odd_length_sum(arr):
    sum_val = 0
    n = len(arr)
    for i in range(n):
        sum_val += ((i+1)*(n-i)+1)//2 * arr[i]
    return sum_val