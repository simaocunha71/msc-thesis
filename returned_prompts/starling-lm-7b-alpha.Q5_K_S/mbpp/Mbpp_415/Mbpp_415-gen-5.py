
def max_Product(nums):
    max_product = -1000
    max_num1, max_num2 = None, None
    for num in nums:
        if max_product < num:
            max_product = num
            max_num2 = max_num1
            max_num1 = num
        elif max_product < (num * max_num1):
            max_product = (num * max_num1)
            max_num2 = num
    return max_num2, max_num1


