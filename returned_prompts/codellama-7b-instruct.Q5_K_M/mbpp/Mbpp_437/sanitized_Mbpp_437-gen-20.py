def remove_odd(my_str: str) -> str:
  return ''.join([char for i, char in enumerate(my_str) if i % 2 == 0])