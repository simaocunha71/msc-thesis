def median_numbers(num1: int, num2: int, num3: int):
    nums = [num1, num2, num3]
    nums.sort()
    return nums[1] if len(nums) % 2 != 0 else (nums[1] + nums[2]) / 2

