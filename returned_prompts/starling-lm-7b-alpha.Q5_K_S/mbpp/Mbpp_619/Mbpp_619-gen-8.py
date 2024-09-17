
def move_num(s: str) -> str:
  nums = '0123456789'
  return ''.join(c for c in s if c not in nums) + ''.join(sorted(c for c in s if c in nums))


