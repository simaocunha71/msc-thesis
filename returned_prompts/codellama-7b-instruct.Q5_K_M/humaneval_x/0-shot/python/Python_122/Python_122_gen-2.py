
def add_elements(arr, k):
    arr.sort()
    sum = 0
    for i in range(k):
        sum += arr[i]
    return sum
