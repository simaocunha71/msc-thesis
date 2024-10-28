def decimal_to_binary(n):
  return bin(n)[2:] if n > 0 else '0' if n == 0 else 'error' if n < 0 else 'error'  # error for negative numbers