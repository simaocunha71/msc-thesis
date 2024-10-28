
def find_Odd_Pair(nums: list,k: int) -> int:
  return sum(map(lambda x: (x ^ k) & 1, nums))


