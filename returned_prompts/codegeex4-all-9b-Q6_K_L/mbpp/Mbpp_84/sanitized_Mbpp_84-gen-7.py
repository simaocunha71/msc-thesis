def sequence(n):
    if n <= 0:
        return None
    if n == 1:
        return 1
    if n == 2:
        return 2
    arr = [1, 2]
    for i in range(2, n):
        arr.append(arr[arr[i-1] - 1] + arr[arr[i-2] - 1])
    return arr[n-1]