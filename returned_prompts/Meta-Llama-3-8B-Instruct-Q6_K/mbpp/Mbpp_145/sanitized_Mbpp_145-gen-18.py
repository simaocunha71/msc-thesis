def max_Abs_Diff(arr):
    if len(arr) == 0:
        raise ValueError("Input array is empty")
    for x in arr:
        if not isinstance(x, (int, float)):
            raise ValueError("Input array contains non-numeric values")
    return max(arr) - min(arr)