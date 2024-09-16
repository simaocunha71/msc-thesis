
def max_sum(arr):
    arr.sort()
    max_sum = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] < arr[i+1]:
            max_sum = max(max_sum, arr[i] + arr[i+1])
    return max_sum
