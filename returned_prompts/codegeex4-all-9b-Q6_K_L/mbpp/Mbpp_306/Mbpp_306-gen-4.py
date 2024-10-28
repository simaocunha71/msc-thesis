def max_sum_increasing_subseq(nums: list,k: int,i: int,n: int) -> int:
  if k == 0 or i == n:
    return 0
  if nums[i] < nums[k]:
    return max(max_sum_increasing_subseq(nums,k+1,i+1,n),max_sum_increasing_subseq(nums,i+1,i+1,n)+nums[i])
  else:
    return max_sum_increasing_subseq(nums,k+1,i+1,n)

