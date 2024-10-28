def find_even_pair(nums: list) -> int:
  pairs = 0
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if (nums[i] ^ nums[j]) % 2 == 0:
        pairs += 1
  return pairs