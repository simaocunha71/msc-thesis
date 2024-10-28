def max_Product(arr):
    if len(arr) < 2:
        return None
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    for x in arr:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2:
            max2 = x
        if x < min1:
            min2 = min1
            min1 = x
        elif x < min2:
            min2 = x
    return max1 * max2 if max1 * max2 > min1 * min2 else (min1, min2)