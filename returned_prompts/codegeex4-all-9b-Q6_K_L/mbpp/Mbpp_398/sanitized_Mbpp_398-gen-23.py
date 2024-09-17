def sum_of_digits(nums: list) -> int:
  return sum(map(lambda num: sum(int(digit) for digit in str(num)), nums))