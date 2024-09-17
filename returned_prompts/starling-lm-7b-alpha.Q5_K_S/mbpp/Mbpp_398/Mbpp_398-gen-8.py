
def sum_of_digits(nums: list) -> int:
  sums = 0
  for num in nums:
    sums += sum(map(int, str(num)))
  return sums


