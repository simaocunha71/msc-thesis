def pair_xor_Sum(nums, n):
  pair_xor_sum = 0
  for i in range(n):
    for j in range(i+1, n):
      pair_xor_sum += nums[i] ^ nums[j]
  return pair_xor_sum