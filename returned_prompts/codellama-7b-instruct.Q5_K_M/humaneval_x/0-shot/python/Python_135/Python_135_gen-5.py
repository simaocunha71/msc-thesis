
def can_arrange(arr):
    if len(arr) <= 1:
        return -1
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return i
    return -1
