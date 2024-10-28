def find_Max_Num(nums: list) -> int:
  nums.sort()
  max_num = int(''.join(map(str,nums[::-1])))
  return max_num