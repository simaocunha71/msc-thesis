def remove_odd(s: str) -> str:
  return "".join(filter(lambda c: ord(c) % 2 == 0, s))