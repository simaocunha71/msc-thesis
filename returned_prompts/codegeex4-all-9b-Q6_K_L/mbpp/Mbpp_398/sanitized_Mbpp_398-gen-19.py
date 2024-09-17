def sum_of_digits(nums: list) -> int:
  sum_nums = 0
  for num in nums:
    sum_nums += sum(int(i) for i in str(num))
  return sum_nums