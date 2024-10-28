
def odd_values_string(string: str) -> str:
  return ''.join(char for i, char in enumerate(string) if i % 2 != 0)


