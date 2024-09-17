
def validate(n: int) -> bool:
  num_str = str(n)
  num_map = {}
  for char in num_str:
    if char in num_map:
      num_map[char] += 1
    else:
      num_map[char] = 1
  for key, value in num_map.items():
    if value > int(key):
      return False
  return True


