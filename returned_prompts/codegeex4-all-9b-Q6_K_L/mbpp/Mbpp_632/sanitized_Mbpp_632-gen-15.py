def move_zero(nums: list) -> list:
  new_list = [i for i in nums if i != 0]
  new_list.extend([0]*(len(nums) - len(new_list)))
  return new_list