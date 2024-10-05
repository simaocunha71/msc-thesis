    def helper(arr, idx_left, idx_right):
        if idx_left > idx_right: return 0
        if arr[idx_left] != arr[idx_right]: return 1
        return helper(arr, idx_left + 1, idx_right - 1) + 1

    return len(arr) - helper(arr, 0, len(arr) - 1)


