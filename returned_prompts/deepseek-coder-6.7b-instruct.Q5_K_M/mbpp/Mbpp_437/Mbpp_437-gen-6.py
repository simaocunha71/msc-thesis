
def remove_odd(string: str) -> str:
  return ''.join([string[i] for i in range(len(string)) if i % 2 == 0])


