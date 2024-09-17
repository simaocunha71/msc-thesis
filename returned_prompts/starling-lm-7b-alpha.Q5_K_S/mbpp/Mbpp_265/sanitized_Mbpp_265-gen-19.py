def list_split(nums: list,n: int) -> list:
  return [nums[i:i+n] for i in range(0,len(nums),n)]