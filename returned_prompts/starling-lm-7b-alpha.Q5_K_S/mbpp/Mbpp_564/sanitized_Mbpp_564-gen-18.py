def count_Pairs(nums: list,n: int) -> int:
  pairs_count = 0
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] != nums[j]:
        pairs_count += 1
  if pairs_count >= n:
    return pairs_count
  else:
    return n