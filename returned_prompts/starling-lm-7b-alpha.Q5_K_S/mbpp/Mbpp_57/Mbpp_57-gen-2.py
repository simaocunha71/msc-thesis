
def find_Max_Num(nums: list) -> int:
  nums.sort(reverse=True)
  nums = str(nums[0]) + "".join(map(str,nums[1:]))
  return int(nums)


