def first_odd(nums):
    for num in nums:
        if num % 2 != 0:
            return num
    return None

assert first_odd([1,3,5]) == 1
assert first_odd([2,4,6]) == None
assert first_odd([2,3,4]) == 3

