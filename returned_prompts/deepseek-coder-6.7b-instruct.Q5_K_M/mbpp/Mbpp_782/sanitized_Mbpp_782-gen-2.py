def odd_length_sum(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        total += ((i+1)*(n-i)+1)//2 * arr[i]
    return total