def odd_length_sum(nums: list) -> int:
  subarrays = []
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      subarrays.append(nums[i:j+1])
  odd_length_subarrays = [subarray for subarray in subarrays if len(subarray) % 2 != 0]
  return sum([sum(subarray) for subarray in odd_length_subarrays])