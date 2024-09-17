
def search(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[l] == arr[m]:
            l = m + 1
        elif arr[m] == arr[r]:
            r = m - 1
        else:
            return arr[l]
    return arr[l]


