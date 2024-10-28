
def max_sum_increasing_subseq(nums: list, i: int, k: int, n: int) -> int:
  max_sum = []
  for j in range(n):
    if j < i:
      max_sum.append(nums[j])
    elif j == i:
      max_sum.append(nums[j] + max(max_sum))
    else:
      max_sum.append(nums[j] + max(max_sum[:k-1]))
  return max(max_sum)


