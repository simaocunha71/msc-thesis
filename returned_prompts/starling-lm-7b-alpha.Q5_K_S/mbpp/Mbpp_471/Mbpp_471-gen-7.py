"""
def find_remainder(nums, mod):
    n = len(nums)
    prod = 1
    for i in range(n):
        prod = (prod * nums[i]) % mod
    return prod

nums = [ 100, 10, 5, 25, 35, 14 ]
mod = 11
print(find_remainder(nums,mod))
"""

# Time complexity: O(n)

def find_remainder(nums, mod):
    if len(nums) == 1:
        return nums[0] % mod
    else:
        return (find_remainder(nums[:len(nums)//2], mod) * find_remainder(nums[len(nums)//2:], mod)) % mod

nums = [ 100, 10, 5, 25, 35, 14 ]
mod = 11
print(find_remainder(nums,mod))
```