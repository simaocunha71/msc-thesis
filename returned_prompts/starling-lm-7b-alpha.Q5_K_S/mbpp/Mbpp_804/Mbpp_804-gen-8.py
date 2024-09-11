"""
def is_product_even(nums):
    product = 1
    for num in nums:
        product *= num
    if product % 2 == 0:
        return True
    else:
        return False
"""

def is_product_even(nums):
    return len([x for x in nums if x%2==0]) > 0

assert is_product_even([1,2,3])
assert is_product_even([2,3,5]) == False
assert is_product_even([2,4])

def is_product_even(nums):
    nums.sort()
    if len(nums) % 2 == 0:
        return True
    else:
        return False



def is_product_even(nums):
    product = 1
    for num in nums:
        product *= num
    if product % 2 == 0:
        return True
    else:
        return False

def is_product_even(nums):
    return 0 not in [x%2 for x in nums]

def is_product_even(nums):
    return len([x for x in nums if x%2==0]) > 0

def is_product_even(nums):
    return len([x for x in nums if x%2==0]) > 0

def is_product_even(nums):
    return len([x for x in nums if x%2==0]) > 0

def is_product_even(nums):
    return len([x for x in nums if x%2==0]) > 0

def is_product_even(nums):
    return len([x for x in nums if x%2==0]) > 0

def is_product_even(nums):
    return len([x for x in nums if x%2==0]) > 0

def is_product_even(nums):
    return len([x for x in nums if x%2==0]) > 0

def is_product_even(nums):
    return len([x