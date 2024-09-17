def find_even_pair(nums: list) -> int:
  even_pair_count = 0
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if (nums[i] ^ nums[j]) % 2 == 0:
        even_pair_count += 1
  return even_pair_count