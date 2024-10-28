def count_char_position(s: str) -> int:
  return sum(1 for i in range(len(s)) if s[i].lower() == chr(97+i))