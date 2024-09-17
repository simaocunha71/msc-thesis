
def odd_length_sum(arr):
    n = len(arr)
    sum = 0
    for i in range(n):
        sum += ((i+1)*(n-i)+1)//2 * arr[i]
    return sum


