
def max_sub_array_sum_repeated(nums: list, k: int, n: int) -> int:
  result = 0
  for i in range(k):
    result = max(result, sum(nums[i:(i+n)]))
  return result


