def decimal_to_binary(n: int) -> str:
  binary_str = bin(n)[2:]
  return binary_str.zfill(len(bin(n)[2:]))