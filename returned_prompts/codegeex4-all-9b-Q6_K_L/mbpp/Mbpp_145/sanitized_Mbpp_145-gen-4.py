def max_Abs_Diff(arr):
    if len(arr) < 2:
        return 0
    return max(max(arr) - min(arr), abs(min(arr) - max(arr)))