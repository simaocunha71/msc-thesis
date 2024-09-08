def max_Product(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two numbers")
    max1, max2 = float('-inf'), float('-inf')
    min1, min2 = float('inf'), float('inf')
    for num in lst:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    return (max1, max2) if max1 * max2 > min1 * min2 else (min1, min2)