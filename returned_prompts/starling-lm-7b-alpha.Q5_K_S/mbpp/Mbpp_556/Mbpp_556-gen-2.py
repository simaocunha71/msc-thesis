
def find_Odd_Pair(nums: list, n: int) -> int:
  return sum(i^n&1 for i in nums)


