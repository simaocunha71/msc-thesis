def _sum(arr):
    if not arr:
        return 0
    for i in arr:
        if not isinstance(i, (int, float)):
            raise ValueError("Array must only contain numbers")
    return sum(arr)