def max_Product(arr):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    result = (None, None)

    for num in arr:
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

        if max1 * max2 > result[0]:
            result = (max1, max2)

    return result