def is_Monotonic(arr):
    if len(arr) <= 1:
        return True
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))