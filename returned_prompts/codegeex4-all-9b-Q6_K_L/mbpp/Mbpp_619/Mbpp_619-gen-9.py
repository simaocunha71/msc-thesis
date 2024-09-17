def move_num(s: str) -> str:
  letters = [c for c in s if not c.isdigit()]
  nums = [c for c in s if c.isdigit()]
  return ''.join(letters) + ''.join(nums)