def move_zero(nums: list) -> list:
  zero_list = []
  for num in nums:
    if num != 0:
      print(num)
    else:
      zero_list.append(num)
  return nums + zero_list