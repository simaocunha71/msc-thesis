def find_Max_Num(nums: list) -> int:
  nums.sort(reverse = True)
  return int("".join(map(str,nums)))