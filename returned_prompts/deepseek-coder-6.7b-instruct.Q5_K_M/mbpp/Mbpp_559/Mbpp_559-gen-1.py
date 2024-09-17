
def max_sub_array_sum(nums: list, n: int) -> int:
  max_sum = 0
  for i in range(n):
    sum = 0
    for j in range(i+1, n):
      sum += nums[j]
      if sum > max_sum:
        max_sum = sum
  return max_sum
"""
This function uses a technique called "Sliding Window" and calculates the sum of the sublists. The sum is compared with the max_sum and if the sum is larger, max_sum is updated. Finally, the max_sum which is the sum of the largest contiguous sublist is returned.
"""

