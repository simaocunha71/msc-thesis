def split_two_parts(nums: list,l: int):
  first_part = nums[:l]
  second_part = nums[l:]
  return (first_part, second_part)