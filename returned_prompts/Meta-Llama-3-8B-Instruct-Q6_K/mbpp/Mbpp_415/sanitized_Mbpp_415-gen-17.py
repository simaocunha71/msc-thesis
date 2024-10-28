def max_Product(arr):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    res = ()
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i
        if i < min1:
            min2 = min1
            min1 = i
        elif i < min2:
            min2 = i
    return (max1, max2) if max1*max2 > max1*min1 and max1*max2 > max2*min2 else (min1, min2)