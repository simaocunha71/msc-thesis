def find_Max_Num(nums: list) -> int:
  nums.sort(reverse=True)
  max_num = 0
  for num in nums:
    max_num = max_num*10 + num
  return max_num