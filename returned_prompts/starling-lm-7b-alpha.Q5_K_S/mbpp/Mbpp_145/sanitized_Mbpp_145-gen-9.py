def max_Abs_Diff(arr):
    maximum = arr[0]
    minimum = arr[0]
    for i in range(len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
        if arr[i] < minimum:
            minimum = arr[i]
    return maximum - minimum