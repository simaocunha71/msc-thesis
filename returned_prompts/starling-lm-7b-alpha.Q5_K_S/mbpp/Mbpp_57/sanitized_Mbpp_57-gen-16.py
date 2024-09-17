def find_Max_Num(nums):
  nums.sort(reverse=True)
  return int(''.join(map(str,nums)))