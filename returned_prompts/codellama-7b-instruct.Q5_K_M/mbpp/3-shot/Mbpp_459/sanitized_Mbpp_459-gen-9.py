def remove_uppercase(s: str) -> str:
  new_string = ''
  for i in range(len(s)):
    if s[i].islower():
      new_string += s[i]
  return new_string