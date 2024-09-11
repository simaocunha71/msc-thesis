def sum_of_digits(nums):
  return sum(sum(map(int, str(i))) for i in nums)  # or sum(sum(int(digit) for digit in str(num)) for num in nums) for a more readable version