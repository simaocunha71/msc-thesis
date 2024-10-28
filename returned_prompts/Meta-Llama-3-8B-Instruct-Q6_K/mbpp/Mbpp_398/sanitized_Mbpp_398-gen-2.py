def sum_of_digits(nums):
    return sum(sum(int(digit) for digit in str(num)) for num in nums)  # or use map(lambda x: sum(int(digit) for digit in str(x)), nums) for Python 3.8 and above