def find_Max_Num(nums: list) -> int:
  return int(''.join(str(num) for num in sorted(nums, reverse=True)))