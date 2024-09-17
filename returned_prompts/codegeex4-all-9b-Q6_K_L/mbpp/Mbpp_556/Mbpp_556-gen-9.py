def find_Odd_Pair(nums: list,n: int) -> int:
  odd_pairs = 0
  for i in range(len(nums)):
      for j in range(i+1, len(nums)):
          if (nums[i] ^ nums[j]) % 2 != 0:
              odd_pairs += 1
  return odd_pairs

