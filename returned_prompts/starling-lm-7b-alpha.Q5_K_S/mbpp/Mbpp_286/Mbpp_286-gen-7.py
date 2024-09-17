
def max_sub_array_sum_repeated(nums: list,k: int,n: int) -> int:
  nums = nums * k
  max_sum = nums[0]
  cur_sum = nums[0]
  for i in range(1,n):
    cur_sum = max(nums[i],cur_sum + nums[i])
    max_sum = max(cur_sum,max_sum)
  return max_sum


