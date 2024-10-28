
def max_sum(arr):
    n = len(arr)
    if n < 3:
        return -1
    inc = [0]*n
    dec = [0]*n
    max_sum = 0
    inc[0] = arr[0]
    dec[n-1] = arr[n-1]
    for i in range(1, n):
        inc[i] = max(inc[i-1], arr[i]) if arr[i] > arr[i-1] else arr[i]
    for i in range(n-2, -1, -1):
        dec[i] = max(dec[i+1], arr[i]) if arr[i] > arr[i+1] else arr[i]
    for i in range(n):
        if inc[i] == dec[i]:
            max_sum = max(max_sum, inc[i])
    for i in range(n-1):
        if inc[i] + dec[i+1] > max_sum:
            max_sum = inc[i] + dec[i+1]
    return max_sum


