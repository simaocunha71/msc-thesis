
def can_arrange(arr):
    largest = -1
    for i in range(len(arr)):
        if arr[i] >= arr[i-1]:
            largest = i
    return largest
