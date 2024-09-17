
def find_min_diff(arr, n):
    diff = arr[1] - arr[0]
    for i in range(1, n-1):
        for j in range(i+1, n):
            if abs(arr[j] - arr[i]) < diff:
                diff = abs(arr[j] - arr[i])
    return diff


