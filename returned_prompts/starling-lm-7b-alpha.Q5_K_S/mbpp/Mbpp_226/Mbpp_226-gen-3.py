
def odd_values_string(s: str) -> str:
  new_str = ''
  for i in range(len(s)):
    if i % 2 != 0:
      new_str += s[i]
  return new_str


