def pancake_sort(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[:i+1], arr[max_index:i+1] = arr[max_index:i+1], arr[:i+1]
    return arr