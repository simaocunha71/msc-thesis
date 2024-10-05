    def check(arr, n):
        if n == 1:
            return True

        if arr[n - 1] > arr[n - 2]:
            return False

        return check(arr, n - 1)

    return check(arr, len(arr))




