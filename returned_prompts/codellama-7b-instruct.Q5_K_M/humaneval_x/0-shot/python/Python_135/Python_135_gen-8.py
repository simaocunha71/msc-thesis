
def can_arrange(arr):
    for i in range(len(arr)):
        if arr[i] >= arr[i-1]:
            continue
        else:
            return i-1
    return -1
