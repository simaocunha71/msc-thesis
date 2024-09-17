def decimal_to_binary(n: int) -> str:
  binary_str = bin(n)[2:]
  if binary_str.startswith('0'):
    return binary_str.lstrip('0')
  return binary_str