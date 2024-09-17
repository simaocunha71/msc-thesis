def max_Product(arr):
    n = len(arr)
    max_x = 1
    max_y = 1

    for i in range(n):
        if arr[i] < 0:
            max_x , max_y = max_y, max_x

        max_x *= arr[i]
        max_y = max(max_y, arr[i])

    if max_x < max_y:
        max_x , max_y = max_y, max_x

    return (max_x, max_y)