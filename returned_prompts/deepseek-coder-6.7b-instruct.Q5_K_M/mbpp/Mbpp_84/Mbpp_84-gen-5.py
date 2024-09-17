
def sequence(n):
    arr = [0, 1, 1]
    for i in range(3, n+1):
        arr.append(arr[arr[i-1]] + arr[i-arr[i-1]])
    return arr[n]


