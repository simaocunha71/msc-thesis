def find_even_pair(nums: list) -> int:
  count = 0
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if (nums[i] ^ nums[j]) & 1 == 0:
        count += 1
  return count