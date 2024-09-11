"""
def max_product_tuple(nums):
    max_product = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            max_product = max(max_product, abs(nums[i][0]*nums[j][0]), abs(nums[i][0]*nums[j][1]), abs(nums[i][1]*nums[j][0]), abs(nums[i][1]*nums[j][1]))
    return max_product


print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)])) # 36
"""

def max_product_tuple(nums):
    max_product = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            max_product = max(max_product, abs(nums[i][0]*nums[j][0]), abs(nums[i][0]*nums[j][1]), abs(nums[i][1]*nums[j][0]), abs(nums[i][1]*nums[j][1]), nums[i][0]*nums[j][1], nums[i][1]*nums[j][0])
    return max_product


print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)])) # 36



# Other solution:
"""
def max_product_tuple(nums):
    return max(map(lambda x:max(map(lambda y:abs(x[0]*y[0]),y)),nums))

print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)])) # 36
"""

# Python3 program to find maximum product of pairs
# in an array of tuples

# Function to find maximum product of pairs
# in an array of tuples
def maxProductPair(arr):
   