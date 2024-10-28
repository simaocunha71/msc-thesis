def find_even_pair(nums: list) -> int:
  return sum((i ^ j) % 2 == 0 for i in nums for j in nums) // 2