def move_zero(nums: list) -> list:
  for num in nums:
    if num == 0:
      nums.remove(num)
      nums.append(num)
  return nums

