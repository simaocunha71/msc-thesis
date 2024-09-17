def list_split(nums: list,n: int) -> list:
  return [nums[i::n] for i in range(n)]