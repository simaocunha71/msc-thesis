def find_Max_Num(nums: list) -> int:
  return int("".join(map(str, sorted(nums, reverse=True))))