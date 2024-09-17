def count_char_position(s):
  s = s.lower()
  return sum(1 for i in range(len(s)) if s[i] == chr(97+i))