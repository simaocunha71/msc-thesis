    def _smallest_change(arr, left, right, count):
        if left > right:
            return count
        if arr[left] == arr[right]:
            return _smallest_change(arr, left + 1, right - 1, count)
        else:
            return _smallest_change(arr, left + 1, right, count + 1)

    return _smallest_change(arr, 0, len(arr) - 1, 0)


