def odd_values_string(s: str) -> str:
  return ''.join([s[i] for i in range(len(s)) if i % 2 == 0])