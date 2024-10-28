def max_Product(nums):
    if not nums:
        return None
    max1 = max2 = float('-inf')
    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return (max1, max2)