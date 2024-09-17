def move_num(s: str) -> str:
  nums = [i for i in s if i.isdigit()]
  non_nums = [i for i in s if not i.isdigit()]
  return ''.join(non_nums) + ''.join(nums)