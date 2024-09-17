def count_Substrings(nums: str) -> int:
  count = 0
  for i in range(len(nums)):
    j = i+1
    sum_digits = int(nums[i])
    while j < len(nums) and sum_digits < j-i+1:
      sum_digits += int(nums[j])
      j += 1
    if j == len(nums) and sum_digits == j-i+1:
      count += 1
  return count