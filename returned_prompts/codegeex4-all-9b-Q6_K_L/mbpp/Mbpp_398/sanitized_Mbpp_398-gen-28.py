def sum_of_digits(nums: list) -> int:
  return sum(map(lambda num: sum(map(int, str(num))), nums))