
def magic_square_test(nums:list):
  if len(nums) != 4:
    return False
  if len(nums[0]) != 4:
    return False
  magic_nums = [8, 1, 6, 3, 5, 7, 4, 9, 2]
  if nums[0][0] != 16 and nums[0][0] != 2:
    return False
  if nums[0][1] != 15 and nums[0][1] != 3:
    return False
  if nums[0][2] != 14 and nums[0][2] != 4:
    return False
  if nums[0][3] != 13 and nums[0][3] != 5:
    return False
  if nums[1][0] != 10 and nums[1][0] != 12:
    return False
  if nums[1][1] != 8 and nums[1][1] != 9:
    return False
  if nums[1][2] != 7 and nums[1][2] != 11:
    return False
  if nums[1][3] != 6 and nums[1][3] != 10:
    return False
  if nums[2][0] != 4 and nums[2][0] != 5:
    return False
  if nums[2][1] != 3 and nums[2][1] != 7:
    return False
  if nums[2][2] != 2 and nums[2][2] != 8:
    return False
  if nums[2][3] != 1 and nums[2][3] != 6:
    return False
  if nums[3][0] != 9 and nums[3][0] != 13:
    return False
  if nums[3][1] != 5 and nums[3][1] != 11:
    return False
  if nums[3][2] != 6 and num