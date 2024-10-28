def shell_sort(arr):
    # 1. Sort the array by using insertion sort
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    # 2. Sort the array by using insertion sort
    for gap in range(len(arr)//2, 0, -1):
        for i in range(gap, len(arr)):
            for j in range(i-gap, 0, -gap):
                if arr[j+gap] < arr[j]:
                    arr[j+gap], arr[j] = arr[j], arr[j+gap]

    return arr