def find_Odd_Pair(nums: list,n: int) -> int:
  count = 0
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if (nums[i] ^ nums[j]) % 2 == 1:
        count += 1
  return count