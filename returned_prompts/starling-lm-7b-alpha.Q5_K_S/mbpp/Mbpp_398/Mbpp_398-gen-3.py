
def sum_of_digits(nums: list) -> int:
  sums = 0
  for i in nums:
    sums += sum(map(int, str(i)))
  return sums


