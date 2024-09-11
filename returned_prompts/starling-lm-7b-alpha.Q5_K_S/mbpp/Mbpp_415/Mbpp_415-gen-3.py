"""
def max_Product(nums):
    max_product = (nums[0], nums[1])
    for i in range(2, len(nums)):
        if nums[i] * max_product[0] > max_product[1] * nums[i]:
            max_product = (max_product[0], nums[i])
        elif nums[i] * max_product[1] > max_product[0] * nums[i]:
            max_product = (nums[i], max_product[1])
    return max_product

print(max_Product([1,2,3,4,7,0,8,4]))
"""

def max_Product(nums):
    max_product = (nums[0], nums[1])
    for i in range(2, len(nums)):
        if nums[i] * max_product[0] > max_product[1] * nums[i]:
            max_product = (max_product[0], nums[i])
        elif nums[i] * max_product[1] > max_product[0] * nums[i]:
            max_product = (nums[i], max_product[1])
    return max_product

print(max_Product([1,2,3,4,7,0,8,4]))


"""
Time Complexity: O(n)
Space Complexity: O(1)

The above solution has a time complexity of O(n) and a constant space complexity. It uses a single for loop to compare the product of the maximum product with the product of the current element and the maximum product. The maximum product is updated if the new product is greater.
"""

"""
Alternate Solution:

def max_Product(nums):
    max_product = (nums[0], nums[1])
    for i in range(2, len(nums)):
        if nums[i] * max_product[0] > max_product[1] * nums[i]:
            max_product = (max_product[0], nums[i])
        elif nums[