def move_num(s: str) -> str:
  nums = [i for i in s if i.isdigit()]
  not_nums = [i for i in s if not i.isdigit()]
  return ''.join(not_nums + nums)