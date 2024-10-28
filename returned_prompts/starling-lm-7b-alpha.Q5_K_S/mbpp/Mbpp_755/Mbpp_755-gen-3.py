
def second_smallest(nums: list) -> int:
  return min(filter(lambda x: x > 0, sorted(nums)[1:]))


