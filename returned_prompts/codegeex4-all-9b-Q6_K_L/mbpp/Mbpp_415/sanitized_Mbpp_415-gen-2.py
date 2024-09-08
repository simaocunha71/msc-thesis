def max_Product(arr):
    max1 = max2 = float('-inf')
    max1_idx = max2_idx = -1

    for i in range(len(arr)):
        if arr[i] > max1:
            max2 = max1
            max2_idx = max1_idx
            max1 = arr[i]
            max1_idx = i
        elif arr[i] > max2:
            max2 = arr[i]
            max2_idx = i

    return (max1, max2)