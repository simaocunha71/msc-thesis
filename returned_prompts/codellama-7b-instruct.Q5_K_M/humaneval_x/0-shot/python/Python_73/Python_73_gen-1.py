
def smallest_change(arr):
    arr.sort()
    min_changes = 0
    for i in range(len(arr)):
        if arr[i] != arr[~i]:
            min_changes += 1
    return min_changes





