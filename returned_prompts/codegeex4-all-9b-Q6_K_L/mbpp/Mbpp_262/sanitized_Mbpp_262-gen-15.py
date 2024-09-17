def split_two_parts(nums: list,L: int):
  first_part = nums[:L]
  second_part = nums[L:]
  return (first_part,second_part)