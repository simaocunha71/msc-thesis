def odd_values_string(s):
  return ''.join([char for i, char in enumerate(s) if i % 2 == 0])  # or s[::2] for a more concise solution