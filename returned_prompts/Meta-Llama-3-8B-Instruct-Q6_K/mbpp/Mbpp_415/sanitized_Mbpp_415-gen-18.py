def max_Product(arr):
    if len(arr) < 2:
        return None
    arr.sort()
    return (arr[-1], arr[-2])