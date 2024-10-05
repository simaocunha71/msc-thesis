    def is_sorted(arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True

    def is_sorted_except_last(arr):
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                return False
        return True

    if not arr:
        return True
    if len(arr) == 1:
        return False
    if is_sorted(arr):
        return False
    if is_sorted_except_last(arr):
        return True
    return False
