
def max_sum_increasing_subseq(nums: list, n: int, k: int, i: int) -> int:
  if n == 0:
    return 0
  if n == 1:
    return nums[0]
  if k == 0:
    return 0
  if k == 1:
    return max(nums)
  if k == n:
    return sum(nums)
  if k > n:
    if n < i:
      return max(nums[:n]) + max(nums[n:]) + nums[k-1]
    else:
      return max(nums[:n-1]) + max(nums[n-1:]) + nums[k-1]
  else:
    return max(nums[:k-1]) + max(nums[k-1:n]) + max(nums[n:])


