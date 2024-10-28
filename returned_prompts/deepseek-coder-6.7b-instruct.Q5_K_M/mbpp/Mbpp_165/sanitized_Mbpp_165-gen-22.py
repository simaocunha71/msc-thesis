def count_char_position(s):
  return sum(1 for a, b in zip(s.lower(), 'abcdefghijklmnopqrstuvwxyz') if a == b)