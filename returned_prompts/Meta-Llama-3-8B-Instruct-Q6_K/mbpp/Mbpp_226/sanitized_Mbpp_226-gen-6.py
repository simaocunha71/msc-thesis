def odd_values_string(s):
  return "".join([c for i, c in enumerate(s) if i % 2 == 0])  # filter out characters with odd indices