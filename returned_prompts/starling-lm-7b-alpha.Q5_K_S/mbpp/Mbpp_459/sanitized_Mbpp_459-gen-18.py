def remove_uppercase(string: str) -> str:
  return ''.join([char for char in string if char.islower()])