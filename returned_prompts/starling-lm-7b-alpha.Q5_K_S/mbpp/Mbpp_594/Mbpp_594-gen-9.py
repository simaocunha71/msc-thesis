def diff_even_odd(nums):
    even = next(filter(lambda x: x % 2 == 0, nums))
    odd = next(filter(lambda x: x % 2 != 0, nums))
    return even - odd

# Another solution
def diff_even_odd(nums):
    even = min(filter(lambda x: x % 2 == 0, nums))
    odd = min(filter(lambda x: x % 2 != 0, nums))
    return even - odd

# Another solution
def diff_even_odd(nums):
    even = filter(lambda x: x % 2 == 0, nums)[0]
    odd = filter(lambda x: x % 2 != 0, nums)[0]
    return even - odd

# Another solution
def diff_even_odd(nums):
    even = [x for x in nums if x % 2 == 0][0]
    odd = [x for x in nums if x % 2 != 0][0]
    return even - odd

# Another solution
def diff_even_odd(nums):
    even = [nums[i] for i, num in enumerate(nums) if num % 2 == 0][0]
    odd = [nums[i] for i, num in enumerate(nums) if num % 2 != 0][0]
    return even - odd

# Another solution
def diff_even_odd(nums):
    even = sorted(nums, key = lambda x : x % 2 == 0)[0]
    odd = sorted(nums, key = lambda x : x % 2 != 0)[0]
    return even - odd

# Another solution
def diff_even_odd(nums):
    even = sorted(nums, key = lambda x : x % 2 == 0)[0]
    odd = sorted(nums, key = lambda x : x % 2 != 0)[0]
    return even - odd

# Another solution
def diff_even_odd(nums):
    even = [num for num in nums if