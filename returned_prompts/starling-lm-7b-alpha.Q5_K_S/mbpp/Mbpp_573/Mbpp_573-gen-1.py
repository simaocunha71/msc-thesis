
def unique_product(nums: list) -> int:
  unique_nums = set(nums)
  return reduce(lambda acc, x: acc * x, unique_nums)


