def is_Monotonic(arr):
    if len(arr)<=2:
        return True
    else:
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))