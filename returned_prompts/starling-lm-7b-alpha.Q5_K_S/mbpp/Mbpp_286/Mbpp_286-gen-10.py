
def max_sub_array_sum_repeated(nums: list,k: int,n: int) -> int:
  for i in range(n):
    nums.append(nums[i])
  max_sum = 0
  curr_sum = 0
  for i in range(len(nums)):
    curr_sum += nums[i]
    if curr_sum > max_sum:
      max_sum = curr_sum
    if curr_sum < 0:
      curr_sum = 0
  return max_sum//k


