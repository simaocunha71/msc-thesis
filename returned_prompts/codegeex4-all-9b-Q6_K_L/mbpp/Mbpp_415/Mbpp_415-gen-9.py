def max_Product(nums: list) -> tuple:
    if len(nums) < 2:
        return None

    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for num in nums:
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

