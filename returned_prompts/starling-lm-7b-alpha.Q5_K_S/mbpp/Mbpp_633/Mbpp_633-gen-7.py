
def pair_xor_Sum(nums: list,n: int) -> int:
  return sum(nums) + sum([i for i in nums[:n] for j in nums[n:] for k in range(1, 2**(len(nums)-2*n)) if i ^ j < 2**(len(nums)-2*n) and (i ^ j) & k == k])


