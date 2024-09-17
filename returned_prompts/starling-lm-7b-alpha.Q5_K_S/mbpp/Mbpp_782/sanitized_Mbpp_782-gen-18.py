def odd_length_sum(nums: list) -> int:
  return sum(sum(nums[i:i+j]) for i in range(0,len(nums),2) for j in range(1,len(nums),2))