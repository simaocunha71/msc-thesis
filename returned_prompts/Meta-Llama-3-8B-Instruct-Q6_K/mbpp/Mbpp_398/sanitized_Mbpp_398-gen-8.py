def sum_of_digits(nums):
    return sum(sum(int(digit) for digit in str(num)) for num in nums)  # Pythonic way
    # return sum(sum(int(digit) for digit in str(num)) for num in nums) # Another way