def shell_sort(arr):
    n = len(arr)
    h = 1
    while h < n/3:
        h = 3*h + 1
    while h >= 1:
        for i in range(h, n):
            for j in range(i, h, -h):
                if arr[j] < arr[j-h]:
                    arr[j], arr[j-h] = arr[j-h], arr[j]
        h = int(h/3)
    return arr

