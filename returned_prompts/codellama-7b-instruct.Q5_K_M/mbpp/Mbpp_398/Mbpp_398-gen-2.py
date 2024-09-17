
def sum_of_digits(nums: list) -> list:
  return [sum(int(i) for i in str(num)) for num in nums]


