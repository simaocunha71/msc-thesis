    def check(arr, i, n):
        if i == n - 1:
            return True
        if arr[i + 1] < arr[i]:
            return False
        return check(arr, i + 1, n)

    if len(arr) == 0:
        return True
    if check(arr, 0, len(arr)):
        return True
    return False


