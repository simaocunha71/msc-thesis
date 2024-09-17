
def remove_uppercase(s: str) -> str:
  return ''.join(filter(str.islower, s))


