def prod_signs(arr):
    if not arr:
        return None
    return sum(abs(x) * (1 if x > 0 else -1 if x < 0 else 0) for x in arr)