
def find_Odd_Pair(nums: list, odd_num: int) -> int:
  odd_count = 0
  for num in nums:
    if (odd_num ^ num) & 1:
      odd_count += 1
  return odd_count


