def sum_of_digits(nums):
  return [sum(map(int, str(num))) for num in nums]